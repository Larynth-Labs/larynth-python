import base64
import binascii
import hashlib
import hmac
import time
from collections.abc import Mapping, Sequence

SECRET_PREFIX = "whsec_"
DEFAULT_TOLERANCE_SECONDS = 300


class WebhookVerificationError(Exception):
    pass


def _key(secret: str) -> bytes:
    raw = secret[len(SECRET_PREFIX) :] if secret.startswith(SECRET_PREFIX) else secret
    try:
        key = base64.b64decode(raw, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise WebhookVerificationError("invalid webhook secret") from exc
    if not key:
        raise WebhookVerificationError("empty webhook secret")
    return key


def _header(headers: Mapping[str, str], name: str) -> str | None:
    for key, value in headers.items():
        if key.lower() == name:
            return value
    return None


def sign(secret: str, msg_id: str, timestamp: int, body: bytes | str) -> str:
    payload = body.encode() if isinstance(body, str) else body
    mac = hmac.new(_key(secret), f"{msg_id}.{timestamp}.".encode() + payload, hashlib.sha256)
    return "v1," + base64.b64encode(mac.digest()).decode()


def verify(
    secrets: str | Sequence[str],
    headers: Mapping[str, str],
    body: bytes | str,
    *,
    tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
    now: float | None = None,
) -> None:
    msg_id = _header(headers, "webhook-id")
    raw_timestamp = _header(headers, "webhook-timestamp")
    signatures = _header(headers, "webhook-signature")
    if not msg_id or not raw_timestamp or not signatures:
        raise WebhookVerificationError("missing webhook headers")
    if not raw_timestamp.isascii() or not raw_timestamp.isdigit():
        raise WebhookVerificationError("invalid webhook-timestamp")
    timestamp = int(raw_timestamp)
    current = time.time() if now is None else now
    if tolerance_seconds > 0 and abs(current - timestamp) > tolerance_seconds:
        raise WebhookVerificationError("webhook-timestamp outside tolerance")
    provided = signatures.split()
    for secret in [secrets] if isinstance(secrets, str) else secrets:
        expected = sign(secret, msg_id, timestamp, body)
        for candidate in provided:
            if hmac.compare_digest(candidate.encode(), expected.encode()):
                return
    raise WebhookVerificationError("no matching signature")

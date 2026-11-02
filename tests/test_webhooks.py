import json
from pathlib import Path

import pytest

from larynth import WebhookVerificationError, sign, verify

VECTORS = json.loads((Path(__file__).resolve().parents[1] / "webhook-vectors.json").read_text())
CASES = VECTORS["cases"]


@pytest.mark.parametrize("case", CASES, ids=[c["name"] for c in CASES])
def test_sign_matches_vector(case):
    assert sign(case["secret"], case["id"], case["timestamp"], case["body"]) == case["signature"]


@pytest.mark.parametrize("v", VECTORS["verify"], ids=[v["name"] for v in VECTORS["verify"]])
def test_verify_vectors(v):
    c = CASES[v["case"]]
    headers = {
        "Webhook-Id": c["id"],
        "Webhook-Timestamp": str(c["timestamp"]),
        "Webhook-Signature": v["header"],
    }
    if v["valid"]:
        verify(c["secret"], headers, c["body"], now=c["timestamp"])
    else:
        with pytest.raises(WebhookVerificationError):
            verify(c["secret"], headers, c["body"], now=c["timestamp"])


def _headers(c):
    return {
        "webhook-id": c["id"],
        "webhook-timestamp": str(c["timestamp"]),
        "webhook-signature": c["signature"],
    }


def test_timestamp_tolerance():
    c = CASES[0]
    verify(c["secret"], _headers(c), c["body"], now=c["timestamp"] + 300)
    for skew in (301, -301):
        with pytest.raises(WebhookVerificationError):
            verify(c["secret"], _headers(c), c["body"], now=c["timestamp"] + skew)


def test_missing_headers_and_tampered_body():
    c = CASES[0]
    with pytest.raises(WebhookVerificationError):
        verify(c["secret"], {}, c["body"])
    with pytest.raises(WebhookVerificationError):
        verify(c["secret"], _headers(c), c["body"] + " ", now=c["timestamp"])


def test_either_secret_during_rotation():
    c = CASES[0]
    other = CASES[1]["secret"]
    verify([other, c["secret"]], _headers(c), c["body"], now=c["timestamp"])
    with pytest.raises(WebhookVerificationError):
        verify([other], _headers(c), c["body"], now=c["timestamp"])


def test_bytes_body():
    c = CASES[0]
    verify(c["secret"], _headers(c), c["body"].encode(), now=c["timestamp"])

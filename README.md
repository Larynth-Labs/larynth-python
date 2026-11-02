# larynth

[![PyPI](https://img.shields.io/pypi/v/larynth)](https://pypi.org/project/larynth/)
[![ci](https://github.com/Larynth-Labs/larynth-python/actions/workflows/ci.yml/badge.svg)](https://github.com/Larynth-Labs/larynth-python/actions/workflows/ci.yml)

Python SDK for the Larynth voice AI API, with webhook signature verification. Full docs: https://docs.larynth.com/sdks/python

## Install

```sh
pip install larynth
```

Requires Python 3.10 or newer.

> **0.x: beta, may change.** Minor versions can include breaking changes until 1.0.

## Authenticate

Create an API key in the Larynth dashboard and keep it in the environment. Never commit it.

```python
import os

from larynth import authenticated_client

client = authenticated_client(
    api_key=os.environ["LARYNTH_API_KEY"],
    base_url="https://api-us.larynth.com",
)
```

## Place a call

Every call needs an idempotency key; replays within 24 hours return the stored response.

```python
import uuid

from larynth.generated.api.calls import create_call
from larynth.generated.models import CreateCallRequest

call = create_call.sync(
    client=client,
    body=CreateCallRequest(
        assistant_id=uuid.UUID("00000000-0000-0000-0000-000000000000"),
        from_e164="+14155550100",
        to_e164="+14155550101",
        purpose="informational",
    ),
    idempotency_key=str(uuid.uuid4()),
)
```

## List assistants

```python
from larynth.generated.api.assistants import list_assistants

assistants = list_assistants.sync(client=client)
```

## Verify a webhook signature

Pass the raw request body, not a re-serialized one.

```python
import os

from larynth import WebhookVerificationError, verify


def handle(headers: dict[str, str], raw_body: bytes) -> int:
    try:
        verify(os.environ["LARYNTH_WEBHOOK_SECRET"], headers, raw_body)
    except WebhookVerificationError:
        return 400
    return 200
```

## About this repository

This SDK is generated from our OpenAPI spec (`openapi/openapi.json`, synced here on every API change), so generated files are overwritten on every sync. Open issues here; pull requests for docs and examples are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

MIT licensed.

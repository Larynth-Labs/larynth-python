import os

import pytest

from larynth import authenticated_client
from larynth.generated.api.assistants import list_assistants
from larynth.generated.api.webhooks import create_webhook, delete_webhook, get_webhook, list_webhooks
from larynth.generated.models.create_webhook_request import CreateWebhookRequest

BASE_URL = os.environ.get("LARYNTH_SMOKE_URL")
API_KEY = os.environ.get("LARYNTH_SMOKE_API_KEY")

pytestmark = pytest.mark.skipif(not (BASE_URL and API_KEY), reason="LARYNTH_SMOKE_URL and LARYNTH_SMOKE_API_KEY are not set")


def test_webhook_endpoint_roundtrip():
    client = authenticated_client(API_KEY, BASE_URL)
    with client:
        assert list_assistants.sync(client=client) is not None

        created = create_webhook.sync(
            client=client,
            body=CreateWebhookRequest(url="https://hooks.example.com/larynth-smoke", event_types=["call.ended"]),
        )
        assert created.secret.startswith("whsec_")
        try:
            fetched = get_webhook.sync(id=created.id, client=client)
            assert fetched.url == "https://hooks.example.com/larynth-smoke"
            page = list_webhooks.sync(client=client)
            assert any(w.id == created.id for w in page.data)
        finally:
            delete_webhook.sync_detailed(id=created.id, client=client)

from salla import Salla
from typing import Union
from salla import (
    ENV,
    Refresh_Token_Payload,
    Salla,
    Webhook_Events,
    WebhookPayload,
    MerchantInfo,
    StoreInfo,
    ErrorToken,
    WebhookResponse,
    EventResponse,
)
import pytest


s = Salla(ENV.ACCESS_TOKEN)


@pytest.mark.asyncio
async def test_merchant_info():
    res = await s.get_merchant_info()
    assert isinstance(res, Union[MerchantInfo, ErrorToken])


@pytest.mark.asyncio
async def test_store_info():
    res = await s.get_store_info()
    assert isinstance(res, Union[StoreInfo, ErrorToken])


@pytest.mark.asyncio
async def test_subscribe_webhook():
    res = await s.webhook_subscribe(
        WebhookPayload(
            name="Ryuk-me",
            event=Webhook_Events.PRODUCT_UPDATED,
            secret=ENV.WEBHOOK_SECRET,
            url="https://webhook.site/2453453-123n7bad6va123",
            security_strategy="token",
        )
    )
    assert isinstance(res, Union[WebhookResponse, ErrorToken])


@pytest.mark.asyncio
async def test_active_webhooks():
    res = await s.get_active_webhooks()
    assert isinstance(res, Union[WebhookResponse, ErrorToken])


@pytest.mark.asyncio
async def test_available_webhooks():
    res = await s.get_available_webhook_events()
    assert isinstance(res, Union[EventResponse, ErrorToken])


@pytest.mark.asyncio
async def test_usubscribewebhooks():
    res = await s.unsubscribe_webhook(url="https://webhook.site/2453453-123n7bad6va123")
    assert isinstance(res, Union[WebhookResponse, ErrorToken])

from salla.base.aiohttpclient import AioHttpClient
from salla.constant import HEADER_CONTENT_APPLICATION_JSON
from salla.schemas.webhook_events import (
    WebhookErrorResposne,
    WebhookPayload,
    WebhookResponse,
)
from typing import Union
from salla.schemas.tokens import ErrorToken


async def subscribe_to_webhook(
    payload: WebhookPayload,
) -> Union[WebhookResponse, ErrorToken]:
    ...

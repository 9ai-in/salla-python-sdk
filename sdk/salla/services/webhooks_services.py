from typing import Union

from salla.base.aiohttpclient import AioHttpClient, aiohttp
from salla.constant import HEADER_CONTENT_APPLICATION_JSON, SUBSCRIBE_WEBHOOK_URL_POST
from salla.schemas.tokens import ErrorToken
from salla.schemas.webhook_events import WebhookPayload, WebhookResponse


async def subscribe_to_webhook(
    payload: WebhookPayload, access_token: str
) -> Union[WebhookResponse, ErrorToken]:
    async with AioHttpClient() as client:
        try:
            __n_headers__ = HEADER_CONTENT_APPLICATION_JSON
            __n_headers__["Authorization"] = "Bearer " + access_token
            resp = await client.post(
                url=SUBSCRIBE_WEBHOOK_URL_POST,
                json=payload.dict(),
                headers=__n_headers__,
            )
            return WebhookResponse(**resp)
        except aiohttp.ClientResponseError as e:
            return ErrorToken(**e.message)

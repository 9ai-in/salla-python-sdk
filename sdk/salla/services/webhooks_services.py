from typing import Union

from salla.base.aiohttpclient import AioHttpClient, aiohttp
from salla.constant import (
    HEADER_CONTENT_APPLICATION_JSON,
    LIST_ACTIVE_WEBHOOKS_GET,
    LIST_WEBHOOK_EVENTS_GET,
    SUBSCRIBE_WEBHOOK_URL_POST,
    WEBHOOK_UNSUBSCRIBE_DELETE,
)
from salla.schemas.tokens import ErrorToken
from salla.schemas.webhook_events import EventResponse, WebhookPayload, WebhookResponse


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


async def unsubscribe_webhook_event(
    access_token: str, id: int = None, url: str = None
) -> Union[WebhookResponse, ErrorToken]:
    async with AioHttpClient() as client:
        try:
            __n_headers__ = HEADER_CONTENT_APPLICATION_JSON
            __n_headers__["Authorization"] = "Bearer " + access_token
            if id:
                _url = WEBHOOK_UNSUBSCRIBE_DELETE + "?id=" + str(id)
            elif url:
                _url = WEBHOOK_UNSUBSCRIBE_DELETE + "?url=" + str(url)
            resp = await client.delete(
                url=_url,
                headers=__n_headers__,
            )
            return WebhookResponse(**resp)
        except aiohttp.ClientResponseError as e:
            return ErrorToken(**e.message)


async def list_active_webhooks(access_token: str) -> Union[WebhookResponse, ErrorToken]:
    async with AioHttpClient() as client:
        try:
            __n_headers__ = HEADER_CONTENT_APPLICATION_JSON
            __n_headers__["Authorization"] = "Bearer " + access_token
            resp = await client.get(
                url=LIST_ACTIVE_WEBHOOKS_GET,
                headers=__n_headers__,
            )
            return WebhookResponse(**resp)
        except aiohttp.ClientResponseError as e:
            return ErrorToken(**e.message)


async def list_webhook_events(access_token: str) -> Union[EventResponse, ErrorToken]:
    async with AioHttpClient() as client:
        try:
            __n_headers__ = HEADER_CONTENT_APPLICATION_JSON
            __n_headers__["Authorization"] = "Bearer " + access_token
            resp = await client.get(
                url=LIST_WEBHOOK_EVENTS_GET,
                headers=__n_headers__,
            )
            return EventResponse(**resp)
        except aiohttp.ClientResponseError as e:
            return ErrorToken(**e.message)

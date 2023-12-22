from typing import Union

from .Config import ENV
from .schemas.merchant import MerchantInfo, StoreInfo
from .schemas.tokens import ErrorToken, Refresh_Token_Payload, Refresh_Token_Response
from .schemas.webhook_events import Webhook_Events, WebhookPayload, WebhookResponse
from .services.auth_services import generate_access_token
from .services.merchant_services import merchant_info, store_info
from .services.webhooks_services import subscribe_to_webhook


class Salla:
    def __init__(self, access_token: str) -> None:
        if access_token is not None:
            self.access_token = access_token
        else:
            raise Exception("access_token cannot be None")

    async def get_access_token_from_refresh_token(
        self, payload: Refresh_Token_Payload
    ) -> Union[Refresh_Token_Response, ErrorToken]:
        return await generate_access_token(payload)

    async def get_merchant_info(
        self,
    ) -> Union[MerchantInfo, ErrorToken]:
        return await merchant_info(self.access_token)

    async def get_store_info(
        self,
    ) -> Union[StoreInfo, ErrorToken]:
        return await store_info(self.access_token)

    async def webhook_subscribe(
        self, payload: WebhookPayload
    ) -> Union[WebhookResponse, ErrorToken]:
        return await subscribe_to_webhook(payload, self.access_token)

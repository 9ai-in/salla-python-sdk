from typing import Optional, Union

from .Config import ENV
from .schemas.merchant import MerchantInfo, StoreInfo
from .schemas.tokens import (
    Access_Token_Payload,
    Access_Token_Response,
    ErrorToken,
    Refresh_Token_Payload,
)
from .schemas.webhook_events import (
    EventResponse,
    Webhook_Events,
    WebhookPayload,
    WebhookResponse,
)
from .services.auth_services import (
    generate_access_token_by_code,
    generate_access_token_by_refresh_token,
)
from .services.merchant_services import merchant_info, store_info
from .services.webhooks_services import (
    list_active_webhooks,
    list_webhook_events,
    subscribe_to_webhook,
    unsubscribe_webhook_event,
)


class Salla:
    def __init__(self, access_token: str) -> None:
        """
        Initialize the Salla API client with the provided access token.

        Args:
            access_token (str): The access token required for API authentication.

        Raises:
            Exception: If access_token is None.
        """
        if access_token is not None:
            self.access_token = access_token
        else:
            raise Exception("access_token cannot be None")

    async def get_access_token_from_refresh_token(
        self, payload: Refresh_Token_Payload
    ) -> Union[Access_Token_Response, ErrorToken]:
        """
        Get a new access token using a refresh token.

        Args:
            payload (Refresh_Token_Payload): Payload containing refresh token information.

        Returns:
            Union[Access_Token_Response, ErrorToken]: Response containing the new access token
            or an error token if the request fails.
        """
        return await generate_access_token_by_refresh_token(payload)

    async def generate_access_token_from_code(
        self, payload: Access_Token_Payload
    ) -> Union[Access_Token_Response, ErrorToken]:
        """
        Get access token using code.

        Args:
            payload (Access_Token_Payload): Payload containing access token information.

        Returns:
            Union[Access_Token_Response, ErrorToken]: Response containing access token
            or an error token if the request fails.
        """
        return await generate_access_token_by_code(payload)

    async def get_merchant_info(
        self,
    ) -> Union[MerchantInfo, ErrorToken]:
        """
        Get information about the merchant associated with the provided access token.

        Returns:
            Union[MerchantInfo, ErrorToken]: Merchant information or an error token if the request fails.
        """
        return await merchant_info(self.access_token)

    async def get_store_info(
        self,
    ) -> Union[StoreInfo, ErrorToken]:
        """
        Get information about the store associated with the provided access token.

        Returns:
            Union[StoreInfo, ErrorToken]: Store information or an error token if the request fails.
        """
        return await store_info(self.access_token)

    async def webhook_subscribe(
        self, payload: WebhookPayload
    ) -> Union[WebhookResponse, ErrorToken]:
        """
        Subscribe to a webhook event.

        Args:
            payload (WebhookPayload): Payload containing webhook subscription information.

        Returns:
            Union[WebhookResponse, ErrorToken]: Response confirming the webhook subscription
            or an error token if the request fails.
        """
        return await subscribe_to_webhook(payload, self.access_token)

    async def unsubscribe_webhook(
        self, id: Optional[int] = None, url: Optional[str] = None
    ) -> Union[WebhookResponse, ErrorToken]:
        """
        Unsubscribe from a webhook event.

        Args:
            id (Optional[int]): The ID of the webhook to unsubscribe from.
            url (Optional[str]): Using url will delete all registered webhooks to this URL.

        Returns:
            Any: Response confirming the webhook unsubscription.
        """
        return await unsubscribe_webhook_event(self.access_token, id, url)

    async def get_active_webhooks(self) -> Union[WebhookResponse, ErrorToken]:
        """
        Get a list of active webhooks.

        Returns:
            Union[WebhookResponse, ErrorToken]: Response containing the list of active webhooks
            or an error token if the request fails.
        """
        return await list_active_webhooks(self.access_token)

    async def get_available_webhook_events(self) -> Union[EventResponse, ErrorToken]:
        """
        Get a list of available webhook events.

        Returns:
            Any: Response containing the list of available webhook events.
        """
        return await list_webhook_events(self.access_token)

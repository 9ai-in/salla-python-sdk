from .schemas.tokens import (
    Refresh_Token_Payload,
    Refresh_Token_Response,
    ErrorToken,
)
from .schemas.merchant import MerchantInfo, StoreInfo
from .services.auth_services import generate_access_token
from .services.merchant_services import merchant_info, store_info
from typing import Union
from .Config import ENV


class Salla:
    def __init__(self, access_token: str) -> None:
        if access_token is not None:
            self.access_token = access_token
        else:
            raise Exception("access_token cannot be None")

    async def get_refresh_token(
        self, payload: Refresh_Token_Payload
    ) -> Union[Refresh_Token_Response, ErrorToken]:
        return await generate_access_token(payload)

    async def get_user_info(
        self,
    ) -> Union[MerchantInfo, ErrorToken]:
        return await merchant_info(self.access_token)

    async def get_store_info(
        self,
    ) -> Union[StoreInfo, ErrorToken]:
        return await store_info(self.access_token)

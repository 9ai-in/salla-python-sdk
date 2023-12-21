from .schemas import tokens
from .services import auth_services
from typing import Union


class Salla:
    def __init__(self, access_token) -> None:
        self.access_token = access_token

    async def get_refresh_token(
        self, payload: tokens.Refresh_Token_Payload
    ) -> Union[tokens.Refresh_Token_Response, tokens.ErrorToken]:
        return await auth_services.generate_access_token(payload)

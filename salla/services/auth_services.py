from salla.base.aiohttpclient import AioHttpClient, aiohttp
from salla.constant import (
    HEADER_FORM_URL_ENCODED,
    REFRESH_TOKEN_URL_POST,
)
from salla.schemas.tokens import (
    Refresh_Token_Response,
    Refresh_Token_Payload,
    ErrorToken,
)
from typing import Union


async def generate_access_token(
    payload: Refresh_Token_Payload,
) -> Union[Refresh_Token_Response, ErrorToken]:
    async with AioHttpClient() as client:
        try:
            resp = await client.post(
                url=REFRESH_TOKEN_URL_POST,
                data=payload.dict(),
                headers=HEADER_FORM_URL_ENCODED,
            )
            return Refresh_Token_Response(**resp)
        except aiohttp.ClientResponseError as e:
            status_code = e.status
            return ErrorToken(status=status_code, **e.message)

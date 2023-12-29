from typing import Union

from salla.base.aiohttpclient import AioHttpClient, aiohttp
from salla.constant import (
    ACCESS_TOKEN_FROM_CODE_POST,
    HEADER_FORM_URL_ENCODED,
    REFRESH_TOKEN_URL_POST,
)
from salla.schemas.tokens import (
    Access_Token_Payload,
    Access_Token_Response,
    ErrorToken,
    Refresh_Token_Payload,
)


async def generate_access_token_by_refresh_token(
    payload: Refresh_Token_Payload,
) -> Union[Access_Token_Response, ErrorToken]:
    async with AioHttpClient() as client:
        try:
            resp = await client.post(
                url=REFRESH_TOKEN_URL_POST,
                data=payload.dict(),
                headers=HEADER_FORM_URL_ENCODED,
            )
            return Access_Token_Response(**resp)
        except aiohttp.ClientResponseError as e:
            status_code = e.status
            return ErrorToken(status=status_code, **e.message)


async def generate_access_token_by_code(
    payload: Access_Token_Payload,
) -> Union[Access_Token_Response, ErrorToken]:
    async with AioHttpClient() as client:
        try:
            resp = await client.post(
                url=ACCESS_TOKEN_FROM_CODE_POST,
                data=payload.dict(),
                headers=HEADER_FORM_URL_ENCODED,
            )
            return Access_Token_Response(**resp)
        except aiohttp.ClientResponseError as e:
            status_code = e.status
            return ErrorToken(status=status_code, **e.message)

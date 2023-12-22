from salla.base.aiohttpclient import AioHttpClient, aiohttp
from salla.constant import (
    HEADER_ACCEPT_APPLICATION_JSON,
    MERCHANT_INFORMATION_URL_GET,
    STORE_INFORMATION_URL_GET,
)
from salla.schemas.tokens import ErrorToken
from salla.schemas.merchant import MerchantInfo, StoreInfo

from typing import Union


async def merchant_info(
    access_token: str,
) -> Union[MerchantInfo, ErrorToken]:
    async with AioHttpClient() as client:
        __n_headers = HEADER_ACCEPT_APPLICATION_JSON
        __n_headers["Authorization"] = "Bearer " + access_token
        try:
            resp = await client.get(
                MERCHANT_INFORMATION_URL_GET, headers=__n_headers
            )
            return MerchantInfo(**resp)
        except aiohttp.ClientResponseError as e:
            return ErrorToken(**e.message)


async def store_info(
    access_token: str,
) -> Union[StoreInfo, ErrorToken]:
    async with AioHttpClient() as client:
        __n_headers = HEADER_ACCEPT_APPLICATION_JSON
        __n_headers["Authorization"] = "Bearer " + access_token
        try:
            resp = await client.get(
                STORE_INFORMATION_URL_GET, headers=__n_headers
            )
            return StoreInfo(**resp)
        except aiohttp.ClientResponseError as e:
            return ErrorToken(**e.message)

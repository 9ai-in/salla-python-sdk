import asyncio
import sys
from typing import Any, Optional

import aiohttp

if (
    sys.version_info[0] == 3
    and sys.version_info[1] >= 8
    and sys.platform.startswith("win")
):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class AioHttpClient:
    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()

    async def get(
        self,
        url: str,
        params: Optional[dict] = None,
        headers: Optional[dict] = None,
        is_json: Optional[bool] = True,
    ):
        async with self.session.get(url, params=params, headers=headers) as response:
            return await self._handle_response(response, is_json)

    async def post(
        self,
        url: str,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
        is_json: Optional[bool] = True,
    ) -> Any:
        async with self.session.post(
            url,
            data=data,
            json=json,
            headers=headers,
        ) as response:
            return await self._handle_response(response, is_json)

    async def _handle_response(
        self,
        response: aiohttp.ClientResponse,
        is_json: Optional[bool] = True,
    ) -> Any:
        if response.ok:
            if is_json:
                return await response.json()
            return await response.text()
        else:
            raise aiohttp.ClientResponseError(
                response.request_info,
                response.history,
                status=response.status,
                message=(await response.json()) or response.reason,
            )

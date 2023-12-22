from salla import (
    Salla,
    Refresh_Token_Payload,
    Refresh_Token_Response,
    ENV,
)
import asyncio


async def main():
    s = Salla(ENV.ACCESS_TOKEN)
    print(await s.get_user_info())
    print("====" * 10)
    print(await s.get_store_info())
    print("+++" * 10)


asyncio.run(main())

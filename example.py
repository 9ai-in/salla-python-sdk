from salla import Salla, tokens
import asyncio


async def main():
    s = Salla("access_token")
    print(
        await s.get_refresh_token(
            payload=tokens.Refresh_Token_Payload(
                client_id="",
                client_secret="",
                refresh_token="",
            )
        )
    )


asyncio.run(main())

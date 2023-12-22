from salla import (
    Salla,
    Refresh_Token_Payload,
    WebhookPayload,
    Webhook_Events,
    ENV,
)
import asyncio


async def main():
    s = Salla(ENV.ACCESS_TOKEN)
    print(await s.get_user_info())
    print("====" * 10)

    print(await s.get_store_info())
    print("+++" * 10)

    wb_payload = WebhookPayload(
        name="Ryuk-wa",
        event=Webhook_Events.PRODUCT_UPDATED,
        secret=ENV.WEBHOOK_SECRET,
        url="https://webhook.site/2453453-123n7bad6va123",
        security_strategy="token",
    )
    print(await s.webhook_subscribe(wb_payload))
    print("---" * 10)

    ref = Refresh_Token_Payload(
        client_id=ENV.CLIENT_ID,
        client_secret=ENV.CLIENT_SECRET,
        refresh_token=ENV.REFRESH_TOKEN,
    )
    print(await s.get_refresh_token(ref))


asyncio.run(main())

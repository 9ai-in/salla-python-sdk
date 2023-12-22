import asyncio

from salla import ENV, Refresh_Token_Payload, Salla, Webhook_Events, WebhookPayload


async def main():
    s = Salla(ENV.ACCESS_TOKEN)
    print(await s.get_merchant_info())
    

    print(await s.get_store_info())

    wb_payload = WebhookPayload(
        name="Ryuk-me",
        event=Webhook_Events.PRODUCT_UPDATED,
        secret=ENV.WEBHOOK_SECRET,
        url="https://webhook.site/2453453-123n7bad6va123",
        security_strategy="token",
    )
    print(await s.webhook_subscribe(wb_payload))

    ref = Refresh_Token_Payload(
        client_id=ENV.CLIENT_ID,
        client_secret=ENV.CLIENT_SECRET,
        refresh_token=ENV.REFRESH_TOKEN,
    )
    print(await s.get_access_token_from_refresh_token(ref))


asyncio.run(main())

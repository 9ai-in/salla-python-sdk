import asyncio

from salla import (
    ENV,
    Refresh_Token_Payload,
    Salla,
    Webhook_Events,
    WebhookPayload,
    Access_Token_Payload,
)


async def main():
    s = Salla(ENV.ACCESS_TOKEN)

    # Get information about the merchant and print it
    await s.get_merchant_info()

    # Get information about the store and print it
    await s.get_store_info()

    # Subscribe to product update events using a webhook
    await s.webhook_subscribe(
        WebhookPayload(
            name="Ryuk-me",
            event=Webhook_Events.PRODUCT_UPDATED,
            secret=ENV.WEBHOOK_SECRET,
            url="https://webhook.site/2453453-123n7bad6va123",
            security_strategy="token",
        )
    )

    # Refresh the access token and print the result
    await s.get_access_token_from_refresh_token(
        Refresh_Token_Payload(
            client_id=ENV.CLIENT_ID,
            client_secret=ENV.CLIENT_SECRET,
            refresh_token=ENV.REFRESH_TOKEN,
        )
    )

    # Get and print a list of active webhooks
    await s.get_active_webhooks()

    # Get and print a list of available webhook events
    await s.get_available_webhook_events()

    # Unsubscribe from a specific webhook and print the result
    await s.unsubscribe_webhook(url="https://webhook.site/2453453-123n7bad6va123")

    await s.generate_access_token_from_code(
        payload=Access_Token_Payload(
            client_id=ENV.CLIENT_ID,
            client_secret=ENV.CLIENT_SECRET,
            code="anabashdghgasdh",
            redirect_uri="https://9ai.in"
            #! Redirection URI should be same which was mentioned in the salla App [Custome mode]
        )
    )


asyncio.run(main())

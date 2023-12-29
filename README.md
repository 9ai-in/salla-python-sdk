<h2 align='center'>Salla SDK 📦</h2>
<p align="center">
<a href="https://github.com/9ai-in"><img title="Author" src="https://img.shields.io/badge/Author-9AI--in-black.svg?style=for-the-badge&logo=github"></a>
<p align="center">
<a href="https://github.com/9ai-in/salla-python-sdk/stargazers/"><img title="Stars" src="https://img.shields.io/github/stars/9ai-in/salla-python-sdk?color=black&style=flat-square"></a>
<a href="https://github.com/9ai-in/salla-python-sdk/network/members"><img title="Forks" src="https://img.shields.io/github/forks/9ai-in/salla-python-sdk?color=black&style=flat-square"></a>
</p>


# Installation

```python
$ install python version 3.10

$ pip install salla-python-sdk

$ create a .env and fill all required fields from .env.example.

```
---

# Supported Features
| Feature                                         | Status |
| ----------------------------------------------- | ------ |
| Generate Access Token From Code                 | ✅      |
| Generate Access Token From Refresh Token        | ✅      |
| Retrive Merchant info                           | ✅      |
| Retrive Store info                              | ✅      |
| Subscribe to a webhook URL                      | ✅      |
| Unsubscribe to a webhook by `url` or `id`       | ✅      |
| List all `registered` and `available` webhook/s | ✅      |

---

# Examples

```python

import asyncio

from salla import ENV, Refresh_Token_Payload, Salla, Webhook_Events, WebhookPayload


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


asyncio.run(main())
```
---


#### License

MIT © [9AI](https://github.com/9AI-IN)
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

$ rename .env.example to .env and fill required fields.

```
---

# Supported Features
| Feature                    | Status |
| -------------------------- | ------ |
| Generate Access Token      | ✅      |
| Retrive Merchant info      | ✅      |
| Retrive Store info         | ✅      |
| Subscribe to a webhook URL | ✅      |

---

# Examples

```python

from salla import Salla, ENV, Refresh_Token_Payload, Webhook_Events, WebhookPayload


async def main():
    s = Salla(ENV.ACCESS_TOKEN)

    print(await s.get_merchant_info())
    

    print(await s.get_store_info())

    wb_payload = WebhookPayload(
        name="product updated,
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
```
---


#### License

MIT © [9AI](https://github.com/9AI-IN)
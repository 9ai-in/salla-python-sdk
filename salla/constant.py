#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!
#!                              HEADERS
#!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HEADER_FORM_URL_ENCODED = {
    "Content-Type": "application/x-www-form-urlencoded"
}
HEADER_APPLICATION_JSON = {"Content-Type": "application/json"}


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!
#!                              URLS
#!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

REFRESH_TOKEN_URL_POST = "https://accounts.salla.sa/oauth2/token"
SUBSCRIBE_WEBHOOK_URL_POST = (
    "https://api.salla.dev/admin/v2/webhooks/subscribe"
)

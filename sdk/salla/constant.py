#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!
#!                              HEADERS
#!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HEADER_FORM_URL_ENCODED = {"Content-Type": "application/x-www-form-urlencoded"}
HEADER_CONTENT_APPLICATION_JSON = {"Content-Type": "application/json"}
HEADER_ACCEPT_APPLICATION_JSON = {"Accept": "application/json"}


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!
#!                              URLS
#!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

REFRESH_TOKEN_URL_POST = "https://accounts.salla.sa/oauth2/token"
SUBSCRIBE_WEBHOOK_URL_POST = "https://api.salla.dev/admin/v2/webhooks/subscribe"
MERCHANT_INFORMATION_URL_GET = "https://api.salla.dev/admin/v2/oauth2/user/info"
STORE_INFORMATION_URL_GET = "https://api.salla.dev/admin/v2/store/info"

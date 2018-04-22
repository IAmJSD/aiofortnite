'''
=========================================
urls.py - Copyright (C) Jake Gealer 2018.
Licensed under the MPL-2.0 license.
https://www.mozilla.org/en-US/MPL/2.0/
=========================================
This file contains URL's which are used across the project.
'''

token_api = (
    "https://account-public-service-prod03.ol.epicgames.com/"
    "account/api/oauth/token"
)
exchange_api = (
    "https://account-public-service-prod03.ol.epicgames.com/"
    "account/api/oauth/exchange"
)
user_lookup_api = (
    "https://persona-public-service-prod06.ol.epicgames.com/"
    "persona/api/public/account/lookup?q={}"
)
br_stats_api = (
    "https://fortnite-public-service-prod11.ol.epicgames.com/"
    "fortnite/api/stats/accountId/{}/bulk/window/alltime"
)
leaderboards_api = (
    "https://fortnite-public-service-prod11.ol.epicgames.com/"
    "fortnite/api/leaderboards/type/global/stat/br_placetop1_"
    "{}_m0{}/window/weekly"
)
account_id_info_api = (
    "https://account-public-service-prod03.ol.epicgames.com/"
    "account/api/public/account?accountId={}"
)
news_api = (
    "https://fortnitecontent-website-prod07.ol.epicgames.com/"
    "content/api/pages/fortnite-game"
)
status_api = (
    "https://lightswitch-public-service-prod06.ol.epicgames."
    "com/lightswitch/api/service/bulk/status?serviceId=Fortnite"
)

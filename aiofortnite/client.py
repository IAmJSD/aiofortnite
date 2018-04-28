'''
===========================================
client.py - Copyright (C) Jake Gealer 2018.
Licensed under the MPL-2.0 license.
https://www.mozilla.org/en-US/MPL/2.0/
===========================================
This file contains the Fortnite client.
'''

from .selfrenewingtokens import SelfRenewingTokens
from .urls import user_lookup_api, br_stats_api, leaderboards_api,\
   account_id_info_api, news_api, status_api
from .abc import User, Platforms, Modes, News
from .caches import UserCache
import asyncio
import aiohttp
import async_timeout
# Imports go here.


class Client:

    def __init__(
        self,
        email,
        password,
        launcher_token,
        fortnite_token,
        loop=asyncio.get_event_loop()
    ):
        self.email = email
        self.password = password
        self.tokens = SelfRenewingTokens(
            launcher_token, fortnite_token, email, password,
            loop
        )
        self.loop = loop
    # Initialises the client.

    async def get_user(self, username, stats=True):

        cached_user = UserCache.get(username)
        if cached_user:
            return cached_user

        try:
            async with aiohttp.ClientSession() as client:
                async with client.get(
                    user_lookup_api.format(username),
                    headers={
                        "Authorization": "bearer {}".format(
                            self.tokens.access_token
                        )
                    }
                ) as response:
                    user_id = (await response.json())["id"]
                if stats:
                    async with client.get(
                        br_stats_api.format(user_id),
                        headers={
                            "Authorization": "bearer {}".format(
                                self.tokens.access_token
                            )
                        }
                    ) as response:
                        stats_json = await response.json()
                else:
                    stats_json = None
            u = User(username, user_id, stats_json)
            UserCache.add(u, 900, self.loop)
            return u
        except BaseException:
            return None
    # Tries to get a user by their username.

    async def get_leaderboards(
        self,
        count=50,
        platform=Platforms.pc,
        mode=Modes.solo,
        stats=True
    ):
        if mode == Modes.all:
            m = Modes.solo
        else:
            m = mode

        mode_key = {
            Modes.all: "_p",
            Modes.squad: "_p9",
            Modes.solo: "_p2",
            Modes.duo: "_p10"
        }
        try:
            m = mode_key[m]
        except KeyError:
            return

        platform_key = {
            Platforms.pc: "pc",
            Platforms.ps4: "ps4",
            Platforms.xbox_one: "xb1"
        }
        try:
            p = platform_key[platform]
        except KeyError:
            return

        url = leaderboards_api.format(
            p, m
        )

        params = {
            "ownertype": 1,
            "itemsPerPage": count
        }

        id2username = {}

        async def get_leaderboard_user(rank, value, _id):
            _id = _id.replace("-", "")

            if _id not in id2username:
                return

            username = id2username[_id]

            cached_user = UserCache.get(username)
            if cached_user:
                cached_user.rank = rank
                cached_user.value = value
                return cached_user

            user = await self.get_user(username, stats=stats)
            UserCache.add(user, 900, self.loop)
            if user:
                user.rank = rank
                user.value = value
                return user

        async with aiohttp.ClientSession() as client:
            async with client.post(
                url,
                params=params,
                headers={
                    "Authorization": "bearer {}".format(
                        self.tokens.access_token
                    ),
                    "content-type": "application/json"
                }
            ) as response:
                entries = (await response.json())["entries"]
                get_url = account_id_info_api.format("&accountId=".join(
                    [
                        player["accountId"].replace("-", "")
                        for player in entries
                    ]
                ))
                async with client.get(
                    get_url,
                    headers={
                        "Authorization": "bearer {}".format(
                            self.tokens.access_token
                        )
                    }
                ) as ur:
                    j = await ur.json()
                    for u in j:
                        id2username[u["id"]] = u["displayName"]
                for player in entries:
                    yield await get_leaderboard_user(
                        player["rank"], player["value"], player["accountId"]
                    )
    # Gets users from the leaderboard.

    async def get_news(self):
        async with aiohttp.ClientSession() as client:
            async with client.get(
                news_api,
                headers={
                    "Accept-Language": "en"
                }
            ) as response:
                br_news = (await response.json())["battleroyalenews"]
                for news in br_news["news"]["messages"]:
                    yield News(news)
    # Returns the current Fortnite Battle Royale news.

    async def get_fortnite_status(self):
        async with aiohttp.ClientSession() as client:
            async with client.get(status_api) as response:
                j = await response.json()
                if j[0]["status"] == "UP":
                    return True
        return False
    # Returns the Fortnite server status.

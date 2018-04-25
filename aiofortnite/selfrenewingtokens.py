'''
=======================================================
autorenewingtokens.py - Copyright (C) Jake Gealer 2018.
Licensed under the MPL-2.0 license.
https://www.mozilla.org/en-US/MPL/2.0/
=======================================================
This file contains a class which loops refreshing the tokens.
'''

import asyncio
import aiohttp
import logging
from datetime import datetime
from .urls import token_api, exchange_api
from .abc import LoginError
# Imports go here.

logger = logging.getLogger("aiofortnite")


class SelfRenewingTokens:
    def __init__(
        self,
        launcher_token,
        fortnite_token,
        email,
        password,
        loop=asyncio.get_event_loop()
    ):
        self.launcher_token = launcher_token
        self.fortnite_token = fortnite_token
        logger.info("Logging in to Fortnite.")
        loop.run_until_complete(self.init_token_fetch(email, password))
        asyncio.ensure_future(self.token_refresh_loop(), loop=loop)

    async def init_token_fetch(self, email, password):
        async with aiohttp.ClientSession() as client:

            async with client.post(
                token_api,
                headers={
                    "Authorization": "basic {}".format(
                        self.launcher_token
                    )
                }, data={
                    "grant_type": "password",
                    "username": "{}".format(email),
                    "password": "{}".format(password),
                    "includePerms": True
                }
            ) as password_response:
                try:
                    j = await password_response.json()
                    access_token = j["access_token"]
                except KeyError:
                    raise LoginError("There was a error getting tokens.")

            async with client.get(
                exchange_api,
                headers={
                    "Authorization": "bearer {}".format(access_token)
                }
            ) as exchange_response:
                j = await exchange_response.json()
                code = j["code"]

            async with client.post(
                token_api,
                headers={
                    "Authorization": "basic {}".format(
                        self.fortnite_token
                    )
                },
                data={
                    "grant_type": "exchange_code",
                    "exchange_code": code,
                    "includePerms": True,
                    "token_type": "egl"
                }
            ) as token_response:
                j = await token_response.json()
                self.access_token = j["access_token"]
                self.refresh_token = j["refresh_token"]
                self.expires_at = datetime.strptime(
                    j["expires_at"],
                    "%Y-%m-%dT%H:%M:%S.%fZ"
                )

    async def token_refresh_loop(self):
        logger.info("Starting the token refresh loop.")
        while True:
            await asyncio.sleep(
                (self.expires_at - datetime.now()).seconds - 30
            )
            logger.info("Refreshing token.")
            async with aiohttp.ClientSession() as client:
                async with client.post(
                    token_api,
                    headers={
                        "Authorization": "basic {}".format(
                            self.fortnite_token
                        )
                    }, data={
                        "grant_type": "refresh_token",
                        "refresh_token": self.refresh_token,
                        "includePerms": True
                    }
                ) as token_update_response:
                    j = await token_update_response.json()
                    self.access_token = j["access_token"]
                    self.expires_at = datetime.strptime(
                        j["expires_at"],
                        "%Y-%m-%dT%H:%M:%S.%fZ"
                    )
                    self.refresh_token = j["refresh_token"]

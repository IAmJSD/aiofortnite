'''
=======================================================
autorenewingtokens.py - Copyright (C) Jake Gealer 2018.
Licensed under the MPL-2.0 license.
https://www.mozilla.org/en-US/MPL/2.0/
=======================================================
This file contains a class which inherits threading.Thread.
It is used for auto-renewing the tokens.
'''

import threading
import requests
import time
from datetime import datetime
from .urls import token_api, exchange_api
from .abc import LoginError
# Imports go here.


class SelfRenewingTokens(threading.Thread):
    def __init__(self, launcher_token, fortnite_token, email, password):
        self.email = email
        self.password = password
        self.launcher_token = launcher_token
        self.fortnite_token = fortnite_token
        super().__init__()
        self.daemon = True
        self.start()
        self.done = False
        while not self.done:
            time.sleep(1)

    def run(self):
        password_response = requests.post(
            token_api,
            headers={
                "Authorization": "basic {}".format(
                    self.launcher_token
                )
            }, data={
                "grant_type": "password",
                "username": "{}".format(self.email),
                "password": "{}".format(self.password),
                "includePerms": True
            }
        ).json()
        try:
            access_token = password_response["access_token"]
        except KeyError:
            raise LoginError("There was a error logging in.")

        exchange_response = requests.get(
            exchange_api,
            headers={
                "Authorization": "bearer {}".format(access_token)
            }
        ).json()
        code = exchange_response["code"]

        token_response = requests.post(
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
        ).json()
        self.access_token = token_response["access_token"]
        refresh_token = token_response["refresh_token"]
        expires_at = datetime.strptime(
            token_response["expires_at"],
            "%Y-%m-%dT%H:%M:%S.%fZ"
        )

        self.done = True

        while True:
            time.sleep(
                (expires_at - datetime.now()).seconds - 30
            )
            token_update_response = requests.post(
                token_api,
                headers={
                    "Authorization": "basic {}".format(self.fortnite_token)
                }, data={
                    "grant_type": "refresh_token",
                    "refresh_token": refresh_token,
                    "includePerms": True
                }
            ).json()
            self.access_token = token_update_response["access_token"]
            expires_at = datetime.strptime(
                token_update_response["expires_at"],
                "%Y-%m-%dT%H:%M:%S.%fZ"
            )
            refresh_token = token_update_response["refresh_token"]

'''
===========================================
caches.py - Copyright (C) Jake Gealer 2018.
Licensed under the MPL-2.0 license.
https://www.mozilla.org/en-US/MPL/2.0/
===========================================
This file stores the various caches.
'''

import asyncio
# Imports go here.


class UserCacheCorpse:
    cache = {}
    usages = {}

    def add(self, user, expiry_time, loop):
        u = user.username.lower()

        self.cache[u] = user

        async def handle_cache_flushing():
            await asyncio.sleep(expiry_time)
            try:
                del self.cache[u]
                del self.usages[u]
            except BaseException:
                pass

        asyncio.ensure_future(handle_cache_flushing(), loop=loop)

    def get(self, username):
        user = self.cache.get(username.lower())

        if not user:
            return

        try:
            self.usages[username] += 1
        except KeyError:
            self.usages[username] = 1

        cache_usage = self.usages[username]

        if cache_usage == 5:
            try:
                del self.cache[username]
                del self.usages[username]
            except BaseException:
                pass

        return user

UserCache = UserCacheCorpse()

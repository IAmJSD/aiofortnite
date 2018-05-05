'''
========================================
abc.py - Copyright (C) Jake Gealer 2018.
Licensed under the MPL-2.0 license.
https://www.mozilla.org/en-US/MPL/2.0/
========================================
This file contains classes which are used across the project.
'''

import sqlite3
import asyncio
from concurrent.futures import ThreadPoolExecutor
# Imports go here.


class Modes:
    solo = "solo"
    duo = "duo"
    squad = "squad"
    all = "all"
# A ABC list of all of the request modes.


class Stat:
    def __init__(self, result):
        self.value = result[0]
        self.mode = result[2]
        self.name = result[3]
# The ABC class for a stat.


class UserStats:
    def __init__(self, stats_json):

        self.db = sqlite3.connect(":memory:")

        cursor = self.db.cursor()

        cursor.execute("""
            CREATE TABLE `stats` (
                `value`	INTEGER NOT NULL,
                `platform`	TEXT NOT NULL,
                `mode`	TEXT NOT NULL,
                `name`	TEXT NOT NULL
            );
        """)

        for stat in stats_json:

            name = stat.get("name")
            value = stat.get("value")

            if name and value:

                platform_name = "other"
                if "pc" in name:
                    platform_name = "pc"
                elif "xb1" in name:
                    platform_name = "xb1"
                elif "ps4" in name:
                    platform_name = "ps4"

                mode_name = "other"
                if "_p9" in name:
                    mode_name = "squad"
                elif "_p10" in name:
                    mode_name = "duo"
                elif "_p2" in name:
                    mode_name = "solo"

                _name = None
                if "score_" in name:
                    _name = "score"
                elif "matchesplayed_" in name:
                    _name = "matches"
                elif "minutesplayed_" in name:
                    _name = "time"
                elif "kills_" in name:
                    _name = "kills"
                elif "placetop1_" in name:
                    _name = "wins"
                elif 'placetop3_' in name:
                    _name = "top3"
                elif 'placetop5_' in name:
                    _name = "top5"
                elif 'placetop6_' in name:
                    _name = "top6"
                elif 'placetop10_' in name:
                    _name = "top10"
                elif 'placetop12_' in name:
                    _name = "top12"
                elif 'placetop25_' in name:
                    _name = "top25"

                if _name:
                    _tuple = (value, platform_name, mode_name, _name, )
                    cursor.execute(
                        "INSERT INTO stats VALUES (?, ?, ?, ?)", _tuple
                    )

        self.db.commit()
        cursor.close()

    async def get(self, mode=None, platform=None):
        def non_async_get():
            sql_parts = []
            sql_tuple = ()

            x = mode and mode != "all"

            if x:
                sql_parts.append("mode = ?")
                sql_tuple += mode,

            if platform:
                sql_parts.append("platform = ?")
                sql_tuple += platform,

            if len(sql_parts) > 0:
                sql = "SELECT * FROM stats WHERE {}".format(
                    " AND ".join(sql_parts)
                )
            else:
                sql = "SELECT * FROM stats"

            cursor = self.db.cursor()
            cursor.execute(sql, sql_tuple)

            results = cursor.fetchall()
            cursor.close()

            if len(results) == 0:
                return

            _json = {}

            for r in results:
                s = Stat(r)
                try:
                    _json[s.mode][s.name] += s.value
                except KeyError:
                    try:
                        _json[s.mode][s.name] = s.value
                    except KeyError:
                        _json[s.mode] = {}
                        _json[s.mode][s.name] = s.value

            if x:
                return _json

            _all = {}
            for k in _json:
                for c in _json[k]:
                    try:
                        _all[c] += _json[k][c]
                    except KeyError:
                        _all[c] = _json[k][c]

            if not mode:
                _json["all"] = _all
                return _json
            else:
                return {"all": _all}

        return (await asyncio.get_event_loop().run_in_executor(
            ThreadPoolExecutor(), non_async_get
        ))

# The ABC class for all user stats.


class User:
    value = None
    rank = None

    def __init__(self, username, user_id, stats_json):
        self.username = username.lower()
        self.id = user_id
        if stats_json:
            self.stats = UserStats(stats_json)
        else:
            self.stats = None
# The user ABC class.


class LoginError(Exception):
    pass
# The ABC class for a error logging in.


class Platforms:
    pc = "pc"
    ps4 = "ps4"
    xbox_one = "xb1"
# A class of all of the platforms.


class News:
    def __init__(self, news_json):
        self.image = news_json["image"]
        self.title = news_json["title"]
        self.body = news_json["body"]
# A ABC class for the news.

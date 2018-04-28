[![Discord](https://img.shields.io/discord/430802154022895616.svg?logo=discord)](https://discord.gg/AEfWXP9)

**THIS PROJECT IS NOT AFFILIATED WITH FORTNITE IN ANY WAY, SHAPE OR FORM.**

# aiofortnite
aiofortnite is a fully async library for Fortnite. Some of the functions were made with the help of https://github.com/nicolaskenner/python-fortnite-api-wrapper/. **This project will always be evolving with new features, feel free to make PR's to help.**

## Installation
Installation as as simple as (assuming `py` is your default Python 3.5.3+ interpreter):
```
py -m pip install aiofortnite
```

# Using the Client

## Authenticating
We will need a few things to get started:
- A Fortnite e-mail address and password.
- A launcher token and Fortnite token (you can get them using https://gist.github.com/Douile/67daa69b59255bcdc390025053dbe295).

Then we can create a file. I will call mine `test.py`. We will first need to import the library and asyncio for later:
```py
import aiofortnite
import asyncio
```
From here we can put the variables we gathered before and define the client:
```py
email = "YOUR_FORTNITE_EMAIL_HERE"
password = "YOUR_FORTNITE_PASSWORD_HERE"
launcher_token = "YOUR_LAUNCHER_TOKEN_HERE"
fortnite_token = "YOUR_FORTNITE_TOKEN_HERE"

fortnite_cli = aiofortnite.Client(
    email=email,
    password=password,
    launcher_token=launcher_token,
    fortnite_token=fortnite_token
)
```
This will then also initialise the background thread used to renew the access tokens.

## Users

Since we are running directly from in Python we will now need to make a loop. Please note if you are using something like `discord.py` you will not need to do this:
```py
async def async_function():
    # This is the async function.

loop = asyncio.get_event_loop()
loop.run_until_complete(async_function())
```

Now in a async function we can use the features of aiofortnite. Lets start simple by checking if Fortnite is up:
```py
key = {
    True: "UP",
    False: "DOWN"
}
up = await fortnite_cli.get_fortnite_status()
print("Fortnite is {}".format(key[up]))
```
Obviously we can do much more complex things than this. To demonstrate, lets fetch a user.
```py
user = await fortnite_cli.get_user("ue4jake")
# The user will be None if there is a error fetching.
```
Users can have the following attributes:
- `username` - The username of the user.
- `id` - The users user ID.
- `value` - This is the users value. This is `None` unless it is fetched from the leaderboards.
- `rank` - This is the users rank. This is `None` unless it is fetched from the leaderboards.
- `stats` - This is a instance of `aiofortnite.abc.UserStats`. More information is listed below.

## Stats

Stats can be fetched as a JSON object. Firstly, we will define the mode and platform:
```py
mode = None
# ----- Modes -----
# None = All modes.
# aiofortnite.Modes.all = Only show stats for all of them combined.
# aiofortnite.Modes.duo = Only show stats for the duo mode.
# aiofortnite.Modes.solo = Only show stats for the solo mode.
# aiofortnite.Modes.squad = Only show stats for the squad mode.
# -----------------

platform = None
# ----- Platforms -----
# None = All platforms.
# aiofortnite.Platforms.pc = Only show stats for the PC platform.
# aiofortnite.Platforms.ps4 = Only show stats for the PS4 platform.
# aiofortnite.Platforms.xbox_one = Only show stats for the XB1 platform.
# aiofortnite.Platforms.other = Only show stats for platforms not implemented yet.
# ---------------------
```

We can then run `user.stats.get(mode=mode, platform=platform)` to get the user stats. They will be formatted so that the root keys in the JSON are the gamemodes and the rest of the stats are keys inside of these. For instance (thanks Elliot [SpaceEll] for giving your username so I could test):
```json
{"duo": {"score": 85866, "matches": 417, "top12": 111, "wins": 18, "time": 1907, "top5": 49, "kills": 573}, "squad": {"score": 172508, "top3": 104, "kills": 851, "matches": 618, "time": 3810, "top6": 160, "wins": 59}, "solo": {"score": 61896, "kills": 530, "matches": 422, "time": 1446, "wins": 5, "top10": 51, "top25": 105}, "all": {"score": 320270, "matches": 1457, "top12": 111, "wins": 82, "time": 7163, "top5": 49, "kills": 1954, "top3": 104, "top6": 160, "top10": 51, "top25": 105}}
```
If you are getting stats for a specific platform, they will only be the stats for that platform. If not, they will be combined with the other platforms.

## Leaderboards
Leaderboards are very simple to use. Firstly, we will need to import some classes from aiofortnite:
```py
from aiofortnite import Platforms, Modes
```
From here, we can pick our platform, how many people we want from the leaderboards and our mode (minus `all`):
```py
mode = Modes.duo
platform = Platforms.pc
count = 10
```
Using the built in async generator we can now pull them down:
```py
async for user in fortnite_cli.get_leaderboards(mode=mode, platform=platform, count=count):
    if user:
        print(user.name)
```

## News
News is extremely simple to pull down:
```py
async for news in fortnite_cli.get_news():
    print(news.title)
    print(news.body)
    print(news.image)
```

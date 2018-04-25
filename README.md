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
- `stats` - Described below. Can be disabled in any function handling users with `stats=False`.

## Stats

Stats have the following attributes repersenting the platforms:
- `pc`
- `ps4`
- `xbox_one`

From here, each platform has the following modes as its attributes:
- `squad`
- `solo`
- `duo`
- `all`

These modes have the following attributes:
- `score`
- `matches`
- `time`
- `kills`
- `wins`
- `top3`
- `top5`
- `top6`
- `top10`
- `top12`
- `top25`

Therefore we can interface with the user like:
```py
print(
    "The amount of kills the user has on PC is: {}".format(user.stats.pc.all.kills)
)
```

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

# Help
If you need any additional help you can do one of the following:
- Add me on Discord and I'll DM you right away. - `JakeMakesStuff#0001`
- Join SSL. - https://discord.me/ssl
- Create a issue here.

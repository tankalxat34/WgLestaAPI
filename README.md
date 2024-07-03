# WgLestaAPI

Unofficial Python library that facilitates working with **<a href="https://developers.wargaming.net"><img src="docs/icons/wg.ico" width=15px> API Wargaming.net</a>** and **<a href="https://developers.lesta.ru"><img src="docs/icons/lesta.ico" width=15px> API Lesta Games</a>** functionality via **Python**.

[![Downloads](https://static.pepy.tech/personalized-badge/wglestaapi?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads)](https://pepy.tech/project/wglestaapi)
[![Downloads](https://static.pepy.tech/personalized-badge/wglestaapi?period=month&units=international_system&left_color=grey&right_color=blue&left_text=downloads/month)](https://pepy.tech/project/wglestaapi)
[![Downloads](https://static.pepy.tech/personalized-badge/wglestaapi?period=week&units=international_system&left_color=grey&right_color=blue&left_text=downloads/week)](https://pepy.tech/project/wglestaapi)
[![Supported Versions](https://img.shields.io/pypi/pyversions/wglestaapi)](https://pypi.org/project/wglestaapi)
[![Version](https://img.shields.io/pypi/v/wglestaapi?color=success)](https://pypi.org/project/wglestaapi)
[![](https://img.shields.io/pypi/format/wglestaapi)](https://pypi.org/project/wglestaapi)
[![](https://img.shields.io/pypi/wheel/wglestaapi)](https://pypi.org/project/wglestaapi)
[![GitHub Repo stars](https://img.shields.io/github/stars/tankalxat34/wglestaapi?style=social)](https://github.com/tankalxat34/wglestaapi)

By downloading this library you fully agree with all official documents **Lesta Games** and **Wargaming.net** about **Lesta Games** and **Wargaming.net** products. *The author of the library ([Alexander Podstrechny](https://github.com/tankalxat34)) is not responsible for your actions performed with the help of this program code.*

> [!NOTE]
> If you like this project please add it to favorite :star: \
> Thanks for your feedback!

## Installing the library

Run the command below at the command line

```
pip install WgLestaAPI
```


## The main advantages

* The presence of synchronous and asynchronous methods of working with the API;
* The ability to use any available methods of the official API through this single library;
* The ability to run a single `*.py` program in several different regions;
* Built-in constants to designate all games and regions for **<a href="https://developers.wargaming.net"><img src="docs/icons/wg.ico" width=15px> API Wargaming.net</a>** and **<a href="https://developers.lesta.ru"><img src="docs/icons/lesta.ico" width=15px> API Lesta Games</a>**;
* One App class with all the necessary library methods.

## Quickstart

### 1. Get an `application_id`
1. Choice your API provider: **<a href="https://developers.wargaming.net"><img src="docs/icons/wg.ico" width=15px> API Wargaming.net</a>** or **<a href="https://developers.lesta.ru"><img src="docs/icons/lesta.ico" width=15px> API Lesta Games</a>**;
2. Log in to the official API provider service;
3. Create a new application by clicking on the button **Add application** or use the existing;
4. Copy ID field from webpage;


<img src="docs/picture1.png" width=900px>

### 2. Write a synchron variant of the "Hello world" example

```python
from WgLestaAPI.Application import App
from WgLestaAPI.Constants import REGION, GAMENAMES
import json

wgApp = App("YOUR_APPLICATION_ID", REGION.EU)

resp = wgApp.execute("account.info", GAMENAMES.SHORTNAMES.WOT, account_id=563982544)
print(json.dumps(resp, indent=2))

```

In the terminal you will see:

```json
{
  "status": "ok",
  "meta": {
    "count": 1
  },
  "data": {
    "563982544": {
      // ...
      "nickname": "tankalxat34",
      "logout_at": 1597741881
    }
  }
}
```


### 3. Write an async variant of the "Hello world" example

```python
from WgLestaAPI.Application import App
from WgLestaAPI.Constants import REGION, GAMENAMES
import json
import asyncio

wgApp = App("YOUR_APPLICATION_ID", REGION.EU)

async def getMyAccount(myId: int):
    return await wgApp.asyncExecute("account.info", GAMENAMES.SHORTNAMES.WOT, account_id=myId)

resp = asyncio.run(getMyAccount(myId=563982544))
print(json.dumps(resp, indent=2))
```

In the terminal you will see:

```json
{
  "status": "ok",
  "meta": {
    "count": 1
  },
  "data": {
    "563982544": {
      // ...
      "nickname": "tankalxat34",
      "logout_at": 1597741881
    }
  }
}
```

### 4. Get URL to login, logout and prolongate `access_token` actions into your application

You can use the library to generate API links for user authorization in your application. This will allow your application to get an access_token, which can be passed as a parameter inside a request to any available API method

```python
from WgLestaAPI.Application import App
from WgLestaAPI.Constants import REGION, GAMENAMES

wgApp = App("YOUR_APPLICATION_ID", REGION.EU)

print(wgApp.login(redirect_uri="https://example.com/")) # url to your hosted web-application
print(wgApp.logout())
print(wgApp.prolongate())
```

In the terminal you will see:

```
https://api.worldoftanks.eu/wot/auth/login/?application_id=YOUR_APPLICATION_ID&redirect_uri=https://example.com/
https://api.worldoftanks.eu/wot/auth/logout/?application_id=YOUR_APPLICATION_ID
https://api.worldoftanks.eu/wot/auth/prolongate/?application_id=YOUR_APPLICATION_ID
```

### 5. Saving frequently called methods

If you use any method very often, you can save its function to a variable. Then you can call the saved method as many times as you want without purposefully passing parameters inside each call.

```python
from WgLestaAPI.Application import App
from WgLestaAPI.Constants import REGION, GAMENAMES

wgApp = App("YOUR_APPLICATION_ID", REGION.EU)

# method saving
getMyAccount = wgApp.createMethod("account.info", GAMENAMES.SHORTNAMES.WOT, account_id=563982544)

for i in range(3):
    print(i, getMyAccount())
```

## Library functionality

The library implements the basic functions of **API Lesta Games** and **API Wargaming.net**. All requests are made through your application, which you previously created on [<img src="docs/icons/lesta.ico" width=14px> Lesta Games](https://developers.lesta.ru/applications/) or on [<img src="docs/icons/wg.ico" width=14px> Wargaming.net](https://developers.wargaming.net/applications/). Some features are listed below:
- Getting information about the player, his equipment and medals.
- Obtaining information about the clan.
- Getting information about vehicles.
- *And other methods.*

## Copyright Notice

<a href="https://developers.lesta.ru/"><img src="docs/icons/lesta_logo.png" width="178px" style="margin: 20px;"></a> <a href="https://developers.wargaming.net/"><img src="docs/icons/wg_logo.png" width="150px" style="margin: 20px;"></a>

- 2024 © Alexander Podstrechnyy. 
    - [tankalxat34@gmail.com](mailto:tankalxat34@gmail.com?subject=lestagamesapi)
    - [VKontakte](https://vk.com/tankalxat34)
    - [Telegram](https://tankalxat34.t.me)
    - [GithHub](https://github.com/tankalxat34/wglestaapi)
- 2024 © Wargaming.net. All rights reserved.
    - [User Support Center](http://support.wargaming.net/)
    - [Official website](https://wargaming.net/)
    - [License Agreement](https://eu.wargaming.net/user_agreement/)
    - [Privacy Policy](https://eu.wargaming.net/privacy_policy/)
- 2024 © Lesta Games. All rights reserved. 
    - [User Support Center](https://lesta.ru/support/)
    - [Official website](https://lesta.ru/)
    - [License Agreement](https://developers.lesta.ru/documentation/rules/agreement/)
    - [Privacy Policy](https://legal.lesta.ru/privacy-policy/)

*This program code is not a product of Lesta Games and was developed according to Lesta Games DPP rules.*

*This program code is not a product of Wargaming.net and is developed according to WG DPP rules.*

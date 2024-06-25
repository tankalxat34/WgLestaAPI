"""
# WgLestaAPI

Unofficial Python library that facilitates working with API Lesta Games and API Wargaming.net functionality via Python. 

By downloading this library you fully agree with all official documents Lesta Games and Wargaming.net about Lesta Games and Wargaming.net products. The author of the library (Alexander Podstrechny) is not responsible for your actions performed with the help of this program code.

## Installing the library

Run the command below at the command line

```
pip install WgLestaAPI
```

## Library functionality

The library implements the basic functions of API Lesta Games and API Wargaming.net. All requests are made through your application, which you previously created on [Lesta Games](https://developers.lesta.ru/applications/) or on [Wargaming.net](https://developers.wargaming.net/applications/). Some features are listed below:
- Getting information about the player, his equipment and medals.
- Obtaining information about the clan.
- Getting information about equipment, equipment mauls.
- And other methods that do not require user authorization.

## Copyright Notice

- 2024 © Alexander Podstrechnyy. 
    - [tankalxat34@gmail.com](mailto:tankalxat34@gmail.com?subject=lestagamesapi)
    - [VKontakte](https://vk.com/tankalxat34)
    - [Telegram](https://tankalxat34.t.me)
    - [GitHub](https://github.com/tankalxat34/wglestaapi)

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

This program code is not a product of Lesta Games and was developed according to Lesta Games DPP rules.

This program code is not a product of Wargaming.net and is developed according to WG DPP rules.


#### Example of use

##### Async way

    >>> from WgLestaAPI import aioApp
    >>> import asyncio
    >>> m = aioApp.Method("account.info", "wot", account_id=563982544, application_id="your_app_id")
    >>> response = asyncio.run(m.execute())
    >>> print(response)
    {'status': 'ok', 'meta': {'count': 1}, 'data': {'563982544': {'client_language': '', ... 'frags': None}, 'nickname': 'tankalxat34', 'logout_at': 1597741881}}


##### No-async way

    >>> from WgLestaAPI import Application
    >>> APP_ID = "YOUR_APP_ID"
    >>> myQuery = Application.Query(application_id=APP_ID)
    >>> myQuery.extend(search="tank", limit=5)
    >>> m = Application.Method(api_method="account.list", game_shortname="wotb", query=myQuery)
    >>> print(m.execute())
    {'status': 'ok', 'meta': {'count': 5}, 'data': [{'nickname': 'tank', 'account_id': 58114596}, {'nickname': 'TANK000', 'account_id': 89075933}, {'nickname': 'tank00000', 'account_id': 901694}, {'nickname': 'tank000000', 'account_id': 1984757}, {'nickname': 'tank00000000', 'account_id': 90784051}]}

"""

__author__ = "Alexander Podstrechnyy"
__email__ = "tankalxat34@gmail.com"
__license__ = "MIT"
__apiholders__ = ["Wargaming.net <https://wargaming.net>", "Lesta Games <https://lesta.ru>"]
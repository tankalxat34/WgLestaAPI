"""
## Introduction

This is an asynchronous version of the library that can be used to make asynchronous requests to Wargaming.net API or Lesta Games API

#### Note that there is no `Query` object in this version - it was removed in order to implement a simpler syntax to use the library. Pass all query parameters directly to `aioApp.Method` as arguments.

## Copyright Notice

- 2023 © Alexander Podstrechnyy. 
    - [tankalxat34@gmail.com](mailto:tankalxat34@gmail.com?subject=lestagamesapi)
    - [VKontakte](https://vk.com/tankalxat34)
    - [Telegram](https://tankalxat34.t.me)
    - [GitHub](https://github.com/tankalxat34/wglestaapi)

- 2023 © Wargaming.net. All rights reserved.
    - [User Support Center](http://support.wargaming.net/)
    - [Official website](https://wargaming.net/)
    - [License Agreement](https://eu.wargaming.net/user_agreement/)
    - [Privacy Policy](https://eu.wargaming.net/privacy_policy/)
    
- 2023 © Lesta Games. All rights reserved. 
    - [User Support Center](https://lesta.ru/support/)
    - [Official website](https://lesta.ru/)
    - [License Agreement](https://developers.lesta.ru/documentation/rules/agreement/)
    - [Privacy Policy](https://legal.lesta.ru/privacy-policy/)

This program code is not a product of Lesta Games and was developed according to Lesta Games DPP rules.

This program code is not a product of Wargaming.net and is developed according to WG DPP rules.


#### Example of use

    >>> from WgLestaAPI import aioApp
    >>> import asyncio
    >>> m = aioApp.Method("account.info", "wot", account_id=563982544, application_id="your_app_id")
    >>> response = asyncio.run(m.execute())
    >>> print(response)
    {'status': 'ok', 'meta': {'count': 1}, 'data': {'563982544': {'client_language': '', ... 'frags': None}, 'nickname': 'tankalxat34', 'logout_at': 1597741881}}
"""


import aiohttp

from . import Constants, Exceptions


def compile_query(d: dict) -> str:
    if not ("url" in d and len(d.keys()) == 1):
        locale_string = str()
        for key in d.keys():
            locale_string += f"{key}={d[key]}&"
        return f"{locale_string}"[:-1]
    else:
        return d["url"].split("?")[1]


class URLConstructor:
    def __init__(self, game_shortname: Constants.GAMENAMES, region: Constants.REGION) -> None:
        """
        Generates the first part of the link for the request

        https://{api}.{game_longname}.{region}/{game_shortname}/

        """
        self.game_shortname = game_shortname
        self.region = region

        self.pattern = "https://{api}.{game_longname}.{region}/{game_shortname}/"

        if self.game_shortname not in Constants.GAMENAMES.SHORTNAMES.ALL:
            raise Exceptions.ShortnameIsNotDefined(value=self.game_shortname)

        if self.region not in Constants.REGION.ALL_CIS:
            raise Exceptions.RegionDoesNotExisting(value=self.region)

        if self.region not in Constants.INFO[self.game_shortname]["region_list"]:
            raise Exceptions.GameDoesNotAppearThisRegion(value=self.region)

    def get(self) -> str:
        """Returns a link to access the API of a particular game"""
        return self.pattern.format(
            api=Constants.INFO[self.game_shortname]["api"],
            game_longname=Constants.INFO[self.game_shortname]["longname"],
            region=self.region,
            game_shortname=self.game_shortname.replace(
                Constants.GAMENAMES.SHORTNAMES.TANKI, Constants.GAMENAMES.SHORTNAMES.WOT)
        )


class Method:
    def __init__(self, api_method: str, game_shortname: Constants.GAMENAMES.SHORTNAMES, region: Constants.REGION = Constants.REGION.EU, type_request: Constants.TYPEREQUESTS = Constants.TYPEREQUESTS.GET, **kwargs) -> None:
        """
        Class for executing API methods in `method_block.method_name` format. Use constants from the `Constants` module of this library to enter parameters.

        api_method:       Executable API method. Syntax: `method_block.method_name`
        game_shortname:   The short name of the game. For example: `wot`, `tanki`, `wotb`, `wows` etc.
        region:           Optional argument. The region in which the game is located. The default is `eu` if `game_shortname` is not equal `tanki`. If you want to get information from game that are extisting only on RU-region - you need to set up `region` argument as `ru`. Pay attention that Mir tankov (Мир танков) are existing only on SU region.
        type_request:     Optional argument. Query type: `GET` or `POST`. The default is `GET`.

        """
        self.api_method = api_method
        self.query = compile_query(kwargs)
        self.game_shortname = game_shortname
        self.region = region
        self.type_request = type_request

        if self.game_shortname == Constants.GAMENAMES.SHORTNAMES.TANKI:
            self.region = Constants.REGION.SU

        try:
            self.method_block, self.method_name = self.api_method.split(".")
        except Exception:
            raise Exceptions.IncorrectMethodDeclaration(self.api_method)

        self.url_constructor = URLConstructor(
            game_shortname=self.game_shortname, region=self.region)

        self.url = self.url_constructor.get(
        ) + f"{self.method_block}/{self.method_name}/?{self.query}"

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self) -> str:
        return f"WgLestaAPI.Application.Method({self.execute()})"

    async def _fetch_data(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                data = await response.json()
                return data

    async def _get_data(self):
        try:
            data = await self._fetch_data()
            return data
        except aiohttp.ClientError as e:
            print(f"Error fetching data: {e}")
            return {}

    async def execute(self):
        return await self._get_data()

    @property
    def docs(self) -> str:
        """Link to the official description of the method at Wargaming.net or Lesta Games"""
        api_holder = Constants.APIHOLDERS.WG
        if self.region in Constants.REGION.CIS:
            api_holder = Constants.APIHOLDERS.LESTA
        return Constants.URL_PATTERNS["docs"].format(api_holder=api_holder, game_shortname=self.game_shortname.replace(Constants.GAMENAMES.SHORTNAMES.TANKI, Constants.GAMENAMES.SHORTNAMES.WOT), method_block=self.method_block, method_name=self.method_name)

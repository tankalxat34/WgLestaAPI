"""
Implementing common methods for running the WgLestaAPI library
"""

import urllib3
import json

from . import Constants
from . import Exceptions


class Query:
    """Query fields in the URL as ?key1=value1&key2=3000"""

    def __init__(self, **kwargs):
        """
        Query fields in the URL as `?key1=value1&key2=3000`
        
        If you want to create a query from parameters - just enter them one by one, or unpack the dictionary with the `**` operator.

        If you have a string url containing query parameters and you want to unpack them, pass only one `url` argument containing the link with query parameters here.
        """
        self.query = kwargs

    def copy(self):
        """Get an object's copy"""
        return Query(**self.dictionary)

    def pop(self, *args: str):
        """Delete field/fields"""
        for key in args:
            self.query.pop(key)

    def extend(self, **kwargs):
        """Adds the specified value keys to the query. If an already existing key is added, its value is replaced by the passed"""
        if not ("url" in self.query and len(self.query.keys()) == 1):
            self.query = {**self.query, **kwargs}
        else:
            self.query = self.parse()
            self.extend(**kwargs)

    def parse(self) -> dict:
        """Get all queries as a dictionary from the link. If url argument is not passed - KeyError is returned"""
        try:
            first_scan = self.query["url"].split("&")
            first_scan[0] = first_scan[0].split("?")[1]

            result = dict()

            for element in first_scan:
                k, v = element.split("=")[0], "=".join(element.split("=")[1:])
                try:
                    result[k] = int(v)
                except Exception:
                    result[k] = v

            return result
        except KeyError:
            raise KeyError("The \"url\" argument was not found!")

    @property
    def string(self) -> str:
        """Get the current query as a string"""
        if not ("url" in self.query and len(self.query.keys()) == 1):
            locale_string = str()
            for key in self.query.keys():
                locale_string += f"{key}={self.query[key]}&"
            return f"{locale_string}"[:-1]
        else:
            return self.query["url"].split("?")[1]

    @property
    def full(self) -> str:
        """Get query in full entry"""
        return "?" + self.string

    @property
    def dictionary(self) -> dict:
        """Get the current query as a dictionary"""
        if not ("url" in self.query and len(self.query.keys()) == 1):
            return self.query
        else:
            return self.parse()


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
            game_shortname=self.game_shortname.replace(Constants.GAMENAMES.SHORTNAMES.TANKI, Constants.GAMENAMES.SHORTNAMES.WOT)
        )


class Method:
    def __init__(self, api_method: str, game_shortname: Constants.GAMENAMES.SHORTNAMES, query: Query, region: Constants.REGION = Constants.REGION.EU, type_request: Constants.TYPEREQUESTS = Constants.TYPEREQUESTS.GET) -> None:
        """
        Class for executing API methods in `method_block.method_name` format. Use constants from the `Constants` module of this library to enter parameters.

        :param api_method       Executable API method. Syntax: `method_block.method_name`
        :param game_shortname   The short name of the game. For example: `wot`, `tanki`, `wotb`, `wows` etc.
        :param query            The `Query` object of this library, necessarily containing `application_id` of your application. Parameters passed to the URL along with the query.
        :param region           Optional argument. The region in which the game is located. The default is `eu` if `game_shortname` is not equal `tanki`. If you want to get information from game that are extisting only on RU-region - you need to set up `region` argument as `ru`. Pay attention that Mir tankov (Мир танков) are existing only on SU region.
        :param type_request     Optional argument. Query type: `GET` or `POST`. The default is `GET`.
        
        """
        self.api_method = api_method
        self.query = query
        self.game_shortname = game_shortname
        self.region = region
        self.type_request = type_request

        if self.game_shortname == Constants.GAMENAMES.SHORTNAMES.TANKI:
            self.region = Constants.REGION.SU

        try:
            self.method_block, self.method_name = self.api_method.split(".")
        except Exception:
            raise Exceptions.IncorrectMethodDeclaration(self.api_method)

        self.http = urllib3.PoolManager()
        self.url_constructor = URLConstructor(game_shortname=self.game_shortname, region=self.region)
        
        self.url = self.url_constructor.get() + f"{self.method_block}/{self.method_name}/{self.query.full}"

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self) -> str:
        return f"WgLestaAPI.Application.Method({self.execute()})"

    def execute(self) -> dict:
        """Executes specified API method. In case of JSON it returns an object of `dict` type. Otherwise it returns `urllib3.response.HTTPResponse` object"""
        res = self.http.request(self.type_request, self.url.lower())
        try:
            return json.loads(res.data)
        except Exception:
            return res

    @property
    def data(self) -> dict:
        """
        Return data from response by key `data`

        :return `dict`:
        """
        return self.execute()["data"]
    
    @property
    def docs(self) -> str:
        """Link to the official description of the method at Wargaming.net or Lesta Games"""
        api_holder = Constants.APIHOLDERS.WG
        if self.region in Constants.REGION.CIS:
            api_holder = Constants.APIHOLDERS.LESTA
        return Constants.URL_PATTERNS["docs"].format(api_holder=api_holder, game_shortname=self.game_shortname.replace(Constants.GAMENAMES.SHORTNAMES.TANKI, Constants.GAMENAMES.SHORTNAMES.WOT), method_block=self.method_block, method_name=self.method_name)
        

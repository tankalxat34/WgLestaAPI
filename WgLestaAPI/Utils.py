from typing import Any, Callable
import aiohttp
import urllib3
import json

from . import Constants
from . import Exceptions


def maskString(s: str) -> str:
    l = int(len(s) // 6)
    return f'{s[:l]}...{s[-l:]}'


def validateQuery(f: Callable):
    def wrapper(*args, **kwargs):
        app_instance = kwargs.get("app_instance") if kwargs.get("app_instance") else args[0]
        region = app_instance.region
        game_shortname = app_instance.game_shortname
        api_method: str = kwargs.get("api_method") if kwargs.get("api_method") else args[1]
        
        if game_shortname not in Constants.GAMENAMES.SHORTNAMES.ALL:
            raise Exceptions.ShortnameIsNotDefined(game_shortname)

        game_section = Constants.SELECTOR[game_shortname]
        if region not in game_section["region"]:
            raise Exceptions.RegionDoesNotExisting(region, game_shortname)
        
        if "." not in api_method or \
            len(api_method.split(".")) != 2:
                raise Exceptions.IncorrectMethodDeclaration(api_method)

        return f(*args, **kwargs)
    return wrapper


def compileQuery(d: dict) -> str:
    """Comvert `dict` to url query string such as `?key1=value1&key2=value2`

    Args:
        d (dict): Dictionary that need to convert

    Returns:
        str: Query string
    """
    res: str = "?"
    for k, v in d.items():
        res += f"{k}={v}&"
    return res[:-1]


def constructUrl(application_id: str, region: str, api_method: str, game_shortname: str, **kwargs) -> str:
    game_section = Constants.SELECTOR[game_shortname]
    method_block, method_name = api_method.split(".")
    query_url: str = compileQuery({"application_id": application_id, **kwargs})
    
    return "https://{api}.{game_longname}.{region}/{game_shortname}/".format(
        api = game_section["api_prefix"],
        region = region,
        game_shortname = game_shortname.replace(Constants.CIS_PREFIX, ""),
        game_longname = game_section["game_longname"],
    ) + f"{method_block}/{method_name}/{query_url}"


@validateQuery
def methodSyncExecute(
        app_instance: Any,
        api_method: str, 
        game_shortname: Constants.GAMENAMES.SHORTNAMES, 
        type_request: Constants.TYPEREQUESTS = "GET",
        **kwargs: dict[str, Any]
    ) -> dict | urllib3.BaseHTTPResponse:
    api_url = constructUrl(app_instance.application_id, app_instance.region, api_method, game_shortname, **kwargs)
    res = app_instance.http.request(type_request, api_url.lower())
    try:
        return json.loads(res.data)
    except Exception:
        return res


@validateQuery
async def methodAsyncExecute(
        app_instance: Any,
        api_method: str, 
        game_shortname: Constants.GAMENAMES.SHORTNAMES, 
        type_request: Constants.TYPEREQUESTS = "GET",
        **kwargs: dict[str, Any]
    ) -> dict | aiohttp.ClientResponse:
    api_url = constructUrl(app_instance.application_id, app_instance.region, api_method, game_shortname, **kwargs)
    async with aiohttp.ClientSession() as session:
        async with session.request(type_request, api_url.lower()) as response:
            try:
                return await response.json()
            except Exception:
                return response


class MethodBlock:
    def __init__(self, 
            app_instance: Any,
            method_block: str
        ) -> None:
        self.app_instance = app_instance
        self.method_block = method_block
        
    def __str__(self) -> str:
        return f"MethodBlock('{self.method_block}')"
    
    def __getattr__(self, method_name: str):
        """Applies dot-notation for methods like `appInstance.methodBlock.methodName(*args, **kwargs)`

        Args:
            method_name (str): Method name from the official documentation
        """
        def dynamicMethod(
                type_request: Constants.TYPEREQUESTS = "GET",
                **kwargs: Any
                ) -> dict | urllib3.BaseHTTPResponse:
            """
            Executes selected method from the official API. 
            
            Args:
                type_request (Constants.TYPEREQUESTS, optional): The type of HTTP request (default is "GET").
                **kwargs (Any): Additional query parameters.

            Returns:
                dict | urllib3.BaseHTTPResponse: The API response, either as a dictionary or raw HTTP response.
            """
            return methodSyncExecute(
                app_instance=self.app_instance,
                api_method=f'{self.method_block}.{method_name}', 
                game_shortname=self.app_instance.game_shortname, 
                type_request=type_request,
                **kwargs
            )
        return dynamicMethod


class AsyncMethodBlock:
    def __init__(self, 
            app_instance: Any,
            method_block: str
        ) -> None:
        self.app_instance = app_instance
        self.method_block = method_block
    
    def __str__(self) -> str:
        return f"AsyncMethodBlock('{self.method_block}')"
    
    def __getattr__(self, method_name: str):
        """Applies dot-notation for methods like `appInstance.methodBlock.methodName(*args, **kwargs)`

        Args:
            method_name (str): Method name from the official documentation
        """
        async def dynamicMethod(
                type_request: Constants.TYPEREQUESTS = "GET",
                **kwargs: Any
                ) -> dict | aiohttp.ClientResponse:
            """
            Executes selected method from the official API. 
            
            Args:
                type_request (Constants.TYPEREQUESTS, optional): The type of HTTP request (default is "GET").
                **kwargs (Any): Additional query parameters.

            Returns:
                dict | aiohttp.ClientResponse: The API response, either as a dictionary or raw HTTP response.
            """
            return await methodAsyncExecute(
                app_instance=self.app_instance,
                api_method=f'{self.method_block}.{method_name}', 
                game_shortname=self.app_instance.game_shortname, 
                type_request=type_request,
                **kwargs
            )
        return dynamicMethod


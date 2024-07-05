"""
Implementing common methods for running the WgLestaAPI library
"""
from typing import Any, Callable
import urllib3
import aiohttp
import json

from . import Utils
from . import Constants
from . import Exceptions


class _AppConstructor:
    """
    DO NOT USE THE RAW `_AppConstructor` TO CREATE A REAL APPLICATION. USE `App` OR `AsyncApp` TO CREATE APP

    A class to interact with the game APIs.
    
    Attributes:
        application_id (str): The application ID for API access.
        region (Constants.REGION): The region for the API access.
        http (urllib3.PoolManager): The HTTP manager for synchronous requests.
    """
    def __init__(self, 
            application_id: str, 
            region: Constants.REGION, 
            game_shortname: Constants.GAMENAMES.SHORTNAMES,
            method_execution: Constants.METHODEXECUTION = Constants.METHODEXECUTION.SYNC
        ) -> None:
        self.application_id = application_id
        self.region = region
        self.game_shortname = game_shortname
        self.method_execution = method_execution
        self.company_name = (Constants.APIHOLDERS.LESTA if self.region in Constants.REGION.CIS else Constants.APIHOLDERS.WG).split('.')[0].capitalize()
        """May be equal `Wargaming` or `Lesta`"""
        
        self.http = urllib3.PoolManager()
    
    def __str__(self) -> str:
        """
        Returns a string representation of the App instance.

        Returns:
            str: A string representing the App instance.
        """
        return f"{self.company_name}App('{Utils.maskString(self.application_id)}')"

    def urlLogin(self, **kwargs: dict[str, Any]) -> str:
        """
        Returns the authentication URL.

        Args:
            **kwargs: Additional query parameters, such as `display`, `expires_at`, `nofollow`, `redirect_uri` or other if needed

        Returns:
            str: The authentication URL.
        """
        api_url = Utils.constructUrl(application_id=self.application_id, region=self.region, api_method="auth.login", game_shortname=Constants.GAMENAMES.SHORTNAMES.TANKI if self.region in Constants.REGION.CIS else Constants.GAMENAMES.SHORTNAMES.WOT, **kwargs)
        return api_url

    def urlLogout(self, **kwargs: dict[str, Any]) -> str:
        """
        Returns the log out URL.

        Args:
            **kwargs: Additional query parameters, such as `access_token` or other if needed

        Returns:
            str: The logout URL.
        """
        api_url = Utils.constructUrl(application_id=self.application_id, region=self.region, api_method="auth.logout", game_shortname=Constants.GAMENAMES.SHORTNAMES.TANKI if self.region in Constants.REGION.CIS else Constants.GAMENAMES.SHORTNAMES.WOT, **kwargs)
        return api_url

    def urlProlongate(self, **kwargs: dict[str, Any]) -> str:
        """
        Returns the URL to prolongate `access_token`. 
        
        Args:
            **kwargs: Additional query parameters, such as `access_token`, `expires_at` or other if needed

        Returns:
            str: The the URL to prolongate existing `access_token`.
        """
        api_url = Utils.constructUrl(application_id=self.application_id, region=self.region, api_method="auth.prolongate", game_shortname=Constants.GAMENAMES.SHORTNAMES.TANKI if self.region in Constants.REGION.CIS else Constants.GAMENAMES.SHORTNAMES.WOT, **kwargs)
        return api_url
    
    def execute(self) -> dict | Any:
        """
        Executes an API request.

        Args:
            api_method (str): The API method to be called.
            type_request (Constants.TYPEREQUESTS, optional): The type of HTTP request (default is "GET").
            **kwargs: Additional query parameters.

        """
        pass
    

class App(_AppConstructor):
    def __init__(self, application_id: str, region: Constants.REGION, game_shortname: Constants.GAMENAMES.SHORTNAMES) -> None:
        """
        Initializes the synchronous App instance with application ID and region.

        Args:
            application_id (str): The application ID for API access.
            region (Constants.REGION): The region for the API access.
            game_shortname (Constants.GAMENAMES.SHORTNAMES): The short name of the game.
        """
        self.method_execution = Constants.METHODEXECUTION.SYNC
        super().__init__(application_id, region, game_shortname, self.method_execution)

    def __getattr__(self, method_block: str, *args, **kwargs) -> Utils.MethodBlock:
        return Utils.MethodBlock(
            app_instance=self,
            method_block=method_block,
            *args, 
            **kwargs
        )

    def execute(
            self, 
            api_method: str, 
            type_request: Constants.TYPEREQUESTS = "GET",
            **kwargs: dict[str, Any]
        ) -> dict | urllib3.BaseHTTPResponse:
        return Utils.methodSyncExecute(
            app_instance=self,
            api_method=api_method, 
            game_shortname=self.game_shortname, 
            type_request=type_request,
            **kwargs
        )


class AsyncApp(_AppConstructor):
    def __init__(self, application_id: str, region: Constants.REGION, game_shortname: Constants.GAMENAMES.SHORTNAMES) -> None:
        """
        Initializes the asynchronous App instance with application ID and region.

        Args:
            application_id (str): The application ID for API access.
            region (Constants.REGION): The region for the API access.
            game_shortname (Constants.GAMENAMES.SHORTNAMES): The short name of the game.
        """
        self.method_execution = Constants.METHODEXECUTION.ASYNC
        super().__init__(application_id, region, game_shortname, self.method_execution)

    def __getattr__(self, method_block: str, *args, **kwargs) -> Utils.AsyncMethodBlock:
        return Utils.AsyncMethodBlock(
            app_instance=self,
            method_block=method_block,
            *args, 
            **kwargs
        )

    async def execute(
            self, 
            api_method: str, 
            type_request: Constants.TYPEREQUESTS = "GET",
            **kwargs: dict[str, Any]
        ) -> dict | aiohttp.ClientResponse:
        return await Utils.methodAsyncExecute(
            app_instance=self,
            api_method=api_method, 
            game_shortname=self.game_shortname, 
            type_request=type_request,
            **kwargs
        )

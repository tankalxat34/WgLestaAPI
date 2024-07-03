from typing import Callable

from . import Constants
from . import Exceptions


def validateQuery(f: Callable):
    def wrapper(*args, **kwargs):
        appInstance = args[0]
        region = appInstance.region
        game_shortname = kwargs.get("game_shortname") if kwargs.get("game_shortname") else args[2]
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



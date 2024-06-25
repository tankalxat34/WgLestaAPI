from . import Utils
from . import Constants
from . import Exceptions

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


def constructUrl(application_id, region, api_method, game_shortname, **kwargs) -> str:
    game_section = Constants.SELECTOR[game_shortname]
    method_block, method_name = api_method.split(".")
    query_url: str = compileQuery({"application_id": application_id, **kwargs})
    
    if region not in game_section["region"]:
        raise Exceptions.RegionDoesNotExisting(region, game_shortname)
    
    return "https://{api}.{game_longname}.{region}/{game_shortname}/".format(
        api = game_section["api_prefix"],
        region = region,
        game_shortname = game_shortname.replace(Constants.CIS_PREFIX, ""),
        game_longname = game_section["game_longname"],
    ) + f"{method_block}/{method_name}/{query_url}"



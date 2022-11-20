"""
Constants for running the WgLestaAPI library
"""

class APIHOLDERS(object):
    """API Owners"""
    WG = "wargaming.net"
    LESTA = "lesta.ru"


class TYPEREQUESTS(object):
    """Request types available for API"""
    GET = "GET"
    POST = "POST"

    ALL = (GET, POST)


class REGION(object):
    """List of regions available for API"""
    RU      = "ru"
    SU      = "su"
    EU      = "eu"
    NA      = "com"
    ASIA    = "asia"
    WGCB    = "com"
    
    CIS     = (RU, SU)                      # Только СНГ
    ALL_CIS = (RU, SU, EU, NA, ASIA, WGCB)  # Включая СНГ
    ALL     = (EU, NA, ASIA, WGCB)          # Не включая СНГ


class GAMENAMES(object):
    """Names of Wargaming.net and Lesta Games games to perform API methods"""
    class SHORTNAMES(object):
        """Short names"""
        WOT     = "wot"     # World of Tanks
        TANKI   = "tanki"   # Мир танков
        WOTB    = "wotb"    # World of Tanks Blitz (Tanks Blitz)
        WOTC    = "wotx"    # World of Tanks Console
        WOWS    = "wows"    # World of Warships (Мир кораблей)
        WOWP    = "wowp"    # World of Warplanes
        WG      = "wgn"     # Wargaming.net

        # All short names
        ALL = (WOT, TANKI, WOTB, WOTC, WOWS, WOWP, WG)

    class LONGNAMES(object):
        """Long names"""
        WOT     = "worldoftanks"        # World of Tanks
        TANKI   = "tanki"               # Мир танков
        WOTB    = "wotblitz"            # World of Tanks Blitz (Tanks Blitz)
        WOTC    = "worldoftanks"        # World of Tanks Console
        WOWS    = "worldofwarships"     # World of Warships (Мир кораблей)
        WOWP    = "worldofwarplanes"    # World of Warplanes
        WG      = "worldoftanks"        # Wargaming.net

        # All long names
        ALL = (WOT, TANKI, WOTB, WOTC, WOWS, WOWP, WG)


URL_PATTERNS = {
    "docs": "https://developers.{api_holder}/reference/all/{game_shortname}/{method_block}/{method_name}/",
    "auth": "https://{api_server}/{api_name}/auth/login/"
}


# selecting the necessary parameters by short game name and region
INFO = {
    # wot
    GAMENAMES.SHORTNAMES.WOT: {
        "api": "api",
        "longname": GAMENAMES.LONGNAMES.WOT,
        "region_list": [REGION.EU, REGION.NA, REGION.ASIA]
    },
    # tanki
    GAMENAMES.SHORTNAMES.TANKI: {
        "api": "api",
        "longname": GAMENAMES.LONGNAMES.TANKI,
        "region_list": [REGION.SU]
    },
    # wotb
    GAMENAMES.SHORTNAMES.WOTB: {
        "api": "api",
        "longname": GAMENAMES.LONGNAMES.WOTB,
        "region_list": [REGION.RU, REGION.EU, REGION.NA, REGION.ASIA]
    },
    # wotc
    GAMENAMES.SHORTNAMES.WOTC: {
        "api": "api-console",
        "longname": GAMENAMES.LONGNAMES.WOTC,
        "region_list": [REGION.WGCB]
    },
    # wows
    GAMENAMES.SHORTNAMES.WOWS: {
        "api": "api",
        "longname": GAMENAMES.LONGNAMES.WOWS,
        "region_list": [REGION.RU, REGION.EU, REGION.NA, REGION.ASIA]
    },
    # wowp
    GAMENAMES.SHORTNAMES.WOWP: {
        "api": "api",
        "longname": GAMENAMES.LONGNAMES.WOWP,
        "region_list": [REGION.EU, REGION.NA]
    },
    # wg
    GAMENAMES.SHORTNAMES.WG: {
        "api": "api",
        "longname": GAMENAMES.LONGNAMES.WG,
        "region_list": [REGION.EU, REGION.NA] # REGION.ASIA does not support all methods
    }
}
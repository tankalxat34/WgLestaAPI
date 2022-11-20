"""
Константы для работы библиотеки

https://{server}/{api_NAME}/{method_block}/{method_name}/?{get_params}

https://api.wotblitz.ru/wotb/account/list/?application_id=2bdc993aef56a8cecd99394db7a1ecca&search=tank&limit=5

https://api.tanki.su/wot/account/list/?application_id=2bdc993aef56a8cecd99394db7a1ecca

https://api.worldoftanks.eu/wot/account/list/
"""

class TYPEREQUESTS(object):
    """Типы запросов, доступные для API"""
    GET = "GET"
    POST = "POST"

    ALL = (GET, POST)

class REGION(object):
    """Перечень доступных для API регионов"""
    RU      = "ru"
    SU      = "su"
    EU      = "eu"
    NA      = "com"
    ASIA    = "asia"
    WGCB    = "com"
    
    CIS = (RU, SU)                          # Только СНГ
    ALL_CIS = (RU, SU, EU, NA, ASIA, WGCB)  # Включая СНГ
    ALL     = (EU, NA, ASIA, WGCB)          # Не включая СНГ


class GAMENAMES(object):
    """Назавания игр Wargaming.net и Lesta Games для выполнения методов API"""
    class SHORTNAMES(object):
        """Короткие названия"""
        WOT     = "wot"     # World of Tanks
        TANKI   = "tanki"   # Мир танков
        WOTB    = "wotb"    # World of Tanks Blitz (Tanks Blitz)
        WOTC    = "wotx"    # World of Tanks Console
        WOWS    = "wows"    # World of Warships (Мир кораблей)
        WOWP    = "wowp"    # World of Warplanes
        WG      = "wgn"     # Wagraming.net

        # Все короткие названия
        ALL = (WOT, TANKI, WOTB, WOTC, WOWS, WOWP, WG)

    class LONGNAMES(object):
        """Длинные названия"""
        WOT     = "worldoftanks"        # World of Tanks
        TANKI   = "tanki"               # Мир танков
        WOTB    = "wotblitz"            # World of Tanks Blitz (Tanks Blitz)
        WOTC    = "worldoftanks"        # World of Tanks Console
        WOWS    = "worldofwarships"     # World of Warships (Мир кораблей)
        WOWP    = "worldofwarplanes"    # World of Warplanes
        WG      = "worldoftanks"        # Wagraming.net

        # Все длинные названия
        ALL = (WOT, TANKI, WOTB, WOTC, WOWS, WOWP, WG)


# выборка необходимых параметров по короткому названию игры и региону
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
        "region_list": [REGION.EU, REGION.NA] # REGION.ASIA поддерживает не все методы
    }
}




PATTERN_URL = "https://{server}/{api_NAME}/{method_block}/{method_name}/?{get_params}"
AUTH_URL = "https://{api_server}/{api_name}/auth/login/"
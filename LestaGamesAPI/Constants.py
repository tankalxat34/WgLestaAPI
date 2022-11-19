"""
Константы
"""


class WOT(object):
    """Константы для игры "Мир танков" """
    name = "tanki"
    server = "tanki.su"
    api_server = "api.tanki.su"
    api_name = "wot"
    readable = "Мир танков"


class WOTB(object):
    """Константы для игры "Tanks Blitz" """
    name = "wotblitz"
    server = "wotblitz.ru"
    api_server = "api.wotblitz.ru"
    api_name = "wotb"
    readable = "Tanks Blitz"


class WOWS(object):
    """Константы для игры "Мир кораблей" """
    name = "worldofwarships"
    server = "worldofwarships.ru"
    api_server = "api.worldofwarships.ru"
    api_name = "wows"
    readable = "Мир кораблей"


PATTERN_URL = "https://{server}/{api_name}/{method_block}/{method_name}/?{get_params}"
AUTH_URL = "https://api.tanki.su/wot/auth/login/"
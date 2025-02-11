"""
Description of errors that occur during operation of the WgLestaAPI library
"""

from . import Constants as c

class RegionDoesNotExisting(Exception):
    def __init__(self, value, game_shortname: str) -> None:
        super().__init__(f"This region \"{value}\" does not existing in API services for the game \"{c.GAMENAMES.LONGNAMES.__dict__[game_shortname.replace(c.CIS_PREFIX, '').upper()]}\". Available regions for this game is: {', '.join(c.SELECTOR[game_shortname]['region'])}")

class ShortnameIsNotDefined(Exception):
    def __init__(self, value) -> None:
        super().__init__(f"This game shortname \"{value}\" is not defined")

class LongnameIsNotDefined(Exception):
    def __init__(self, value) -> None:
        super().__init__(f"This game longname \"{value}\" is not defined")

class GameDoesNotAppearThisRegion(Exception):
    def __init__(self, value) -> None:
        super().__init__(f"This game does not appear in this region: \"{value}\"")

class IncorrectMethodDeclaration(Exception):
    def __init__(self, value) -> None:
        super().__init__(f"Invalid declaration of this method: \"{value}\". You are using ({len(value.split('.'))}) parts of method instead of (2). Also you need use the dot-notation (for example `account.info`)")

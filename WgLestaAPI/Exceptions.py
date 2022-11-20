"""
Описание ошибок, возникающих при работе библиотеки
"""

class RegionDoesNotExisting(Exception):
    def __init__(self, value) -> None:
        super().__init__(f"This region \"{value}\" does not existing in API services")


class ShortnameIsNotDefined(Exception):
    def __init__(self, value) -> None:
        super().__init__(f"This game shorname \"{value}\" is not defined")

class GameDoesNotAppearThisRegion(Exception):
    def __init__(self, value) -> None:
        super().__init__(f"This game does not appear in this region: \"{value}\"")


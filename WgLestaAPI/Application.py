"""
Реализация общих методов для работы библиотеки
"""

import urllib3
import json

from . import Constants
from . import Exceptions


class Query:
    """Поля запроса в URL в виде ?key1=value1&key2=3000"""

    def __init__(self, **kwargs):
        """
        Класс для работы с полями запроса. 

        Для того, чтобы распарсить query из url - передайте сюда один аргумент url
        """
        self.query = kwargs

    def pop(self, *args):
        """Удаляет поле/поля"""
        for key in args:
            self.query.pop(key)

    def extend(self, **kwargs):
        """Добавляет указанные ключи-значения в query. Если добавляется уже существующий ключ - его значение заменяется на переданное"""
        if not ("url" in self.query and len(self.query.keys()) == 1):
            self.query = {**self.query, **kwargs}
        else:
            self.query = self.parse()
            self.extend(**kwargs)

    def parse_per_symbol(self) -> dict:
        """Аналог self.parse(), однако данный метод обрабатывает строку query посимвольно, а не через split"""
        try:
            string_for_view = "?".join(self.query["url"].split("?")[1:])
            locale_key = ""
            locale_value = ""
            flag = False
            for s in string_for_view:
                if s == "=":
                    flag = True

                if flag:
                    locale_value += s
                else:
                    locale_key += s

            return string_for_view

        except KeyError:
            raise KeyError("The \"url\" argument was not found!")

    def parse(self) -> dict:
        """Получить из ссылки все query в виде словаря. Если не передан аргумент url - возвращается ошибка KeyError"""
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
        """Получить текущий query в виде строки"""
        if not ("url" in self.query and len(self.query.keys()) == 1):
            locale_string = str()
            for key in self.query.keys():
                locale_string += f"{key}={self.query[key]}&"
            return f"{locale_string}"[:-1]
        else:
            return self.query["url"].split("?")[1]

    @property
    def full(self) -> str:
        """Получить query в полной записи"""
        return "?" + self.string

    @property
    def dictionary(self) -> dict:
        """Получить текущий query в виде словаря"""
        if not ("url" in self.query and len(self.query.keys()) == 1):
            return self.query
        else:
            return self.parse()


class URLConstructor:
    def __init__(self, game_shortname: Constants.GAMENAMES, region: Constants.REGION) -> None:
        """
        Генирирует первую часть ссылки для запроса

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
        """Возвращает ссылку для доступа к API конкретной игры"""
        return self.pattern.format(
            api=Constants.INFO[self.game_shortname]["api"],
            game_longname=Constants.INFO[self.game_shortname]["longname"],
            region=self.region,
            game_shortname=self.game_shortname.replace(Constants.GAMENAMES.SHORTNAMES.TANKI, Constants.GAMENAMES.SHORTNAMES.WOT)
        )


class App:
    def __init__(self, application_id: str = ""):
        self.application_id = application_id
        self.http = urllib3.PoolManager()

    def execute(self, method: str, full_url: str) -> dict:
        """Выполняет запрос на сервер и возвращает ответ"""
        res = self.http.request(method, full_url)
        try:
            return json.loads(res.data)
        except Exception:
            return res.data


class Method:
    def __init__(self, game: str, method: str, query: Query, type_request: Constants.TYPEREQUESTS, region: str = Constants.REGION) -> None:
        """Выполнение методов в формате method_block.method_name"""
        self.method = method
        self.query = query

        self.method_block, self.method_name = self.method.split(".")

        self.http = urllib3.PoolManager()

    def execute(self) -> dict:
        # "https://{server}/{api_NAME}/{method_block}/{method_name}/?{get_params}"
        # resonse = self.http.request(self.type_request, Constants.PATTERN_URL.format(server=))
        pass

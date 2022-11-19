"""
Реализация общих методов для работы библиотеки
"""

import urllib3
import json

from . import Constants


class Query:
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

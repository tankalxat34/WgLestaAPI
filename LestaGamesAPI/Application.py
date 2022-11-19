"""
Реализация общих методов для работы библиотеки
"""

import urllib3
import json

from . import Constants


class Query:
    def __init__(self, **kwargs):
        """Класс для работы с полями запроса"""
        self.query = kwargs

    def extend(self, **kwargs) -> bool:
        self.query = {**self.query, **kwargs}

    @property
    def string(self):
        locale_string = str()
        for key in self.query.keys():
            locale_string += f"{key}={self.query[key]}&"
        return f"{locale_string}"[:-1]

    @property
    def dictionary(self):
        return self.query


class App:
    def __init__(self, application_id: str = ""):
        self.application_id = application_id
        self.http = urllib3.PoolManager()

    def execute(self, method: str, full_url: str) -> dict:
        """Выполняет запрос на сервер и возвращает ответ"""
        res = self.http.request(method, full_url)
        return json.loads(res.data)

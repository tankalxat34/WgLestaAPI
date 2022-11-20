"""
Модуль для аутентификации пользователя и получения соответствующего временного access_token
"""

import urllib3
import json

from . import Constants
from . import Application

NAME = "tanki"
SERVER = "tanki.su"
API_SERVER = "api.tanki.su"
API_NAME = "wot"
READABLE = "Мир танков"


class UserAuth:
    def __init__(self, application_id: str, **kwargs):
        self.application_id = application_id
        self.app = Application.App(self.application_id)
        self.kwargs = kwargs

    def execute(self):
        return self.app.execute("GET", Constants.AUTH_URL + Application.Query(application_id=self.application_id, nofollow=1, display="page", **self.kwargs).full)

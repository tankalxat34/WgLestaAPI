"""
### WgLestaAPI

Неофициальная Python библиотека, облегчающая работу с функционалом API Lesta Games. Скачивая данную библиотеку вы полностью соглашаетесь со всеми официальными документами Lesta Games об использовании продуктов Lesta Games. Автор библиотеки (Alexander Podstrechnyy) не несет ответственности за ваши действия, совершенные с помощью данного программного кода.


#### Функционал библиотеки

Поддерживается следующий перечень игр: "Мир танков", "Мир кораблей" и "Tanks Blitz".

В библиотеке реализованы основные функции API Lesta Games и API Wargaming.net. Все запросы делаются через ваше приложение, которое вы заранее создали на сайте [Lesta Games](https://developers.lesta.ru/applications/) или на сайте [Wargaming.net](https://developers.wargaming.net/applications/). Некоторые функции перечислены ниже:
- Получение информации об игроке, его техники и медалях.
- Получение информации о клане.
- Получение информации о технике, молулях техники.
- и другие методы, не требующие авторизации пользователя.

Описания методов и полей взяты с официального сайта Lesta Games.

#### Уведомление об авторских правах

- 2022 © Alexander Podstrechnyy. Контакты: 
    - [GitHub](https://github.com/tankalxat34/WgLestaAPI)
    - [tankalxat34@gmail.com](mailto:tankalxat34@gmail.com?subject=lestagamesapi)
    - [ВКонтакте](https://vk.com/tankalxat34)
    - [Telegram](https://tankalxat34.t.me)
- 2022 © Wargaming.net. Все права защищены.
    - [Центр поддержки пользователей](http://support.wargaming.net/)
    - [Официальный сайт](https://wargaming.net/)
    - [Лицензионное соглашение](https://eu.wargaming.net/user_agreement/)
    - [Политика конфиденциальности](https://eu.wargaming.net/privacy_policy/)
- 2022 © Lesta Games. Все права защищены. 
    - [Центр поддержки пользователей](https://lesta.ru/support/)
    - [Официальный сайт](https://lesta.ru/)
    - [Лицензионное соглашение](https://developers.lesta.ru/documentation/rules/agreement/)
    - [Политика конфиденциальности](https://legal.lesta.ru/privacy-policy/)

Данный программный код не является продуктом Lesta Games и разработан согласно правилам Lesta Games DPP.
Данный программный код не является продуктом Wargaming.net и разработан согласно правилам WG DPP.

#### Пример работы

    >>> from WgLestaAPI import Application
    >>> APP_ID = "YOUR_APP_ID"
    >>> myQuery = Application.Query(application_id=APP_ID)
    >>> myQuery.extend(search="tank", limit=5)
    >>> m = Application.Method(api_method="account.list", game_shortname="wotb", query=myQuery)
    >>> print(m.execute())
    {'status': 'ok', 'meta': {'count': 5}, 'data': [{'nickname': 'tank', 'account_id': 58114596}, {'nickname': 'TANK000', 'account_id': 89075933}, {'nickname': 'tank00000', 'account_id': 901694}, {'nickname': 'tank000000', 'account_id': 1984757}, {'nickname': 'tank00000000', 'account_id': 90784051}]}

"""

__author__ = "Alexander Podstrechnyy"
__email__ = "tankalxat34@gmail.com"
__version__ = "0.1.0"
__license__ = "MIT"
__apiholders__ = ["Wargaming.net <https://wargaming.net>", "Lesta Games <https://lesta.ru>"]
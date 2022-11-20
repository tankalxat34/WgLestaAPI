# WgLestaAPI

Неофициальная Python библиотека, облегчающая работу с функционалом **API Lesta Games** и **API Wargaming.net** через **Python**. 

[![Downloads](https://static.pepy.tech/personalized-badge/wglestaapi?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads)](https://pepy.tech/project/wglestaapi)
[![Downloads](https://static.pepy.tech/personalized-badge/wglestaapi?period=month&units=international_system&left_color=grey&right_color=blue&left_text=downloads/month)](https://pepy.tech/project/wglestaapi)
[![Downloads](https://static.pepy.tech/personalized-badge/wglestaapi?period=week&units=international_system&left_color=grey&right_color=blue&left_text=downloads/week)](https://pepy.tech/project/wglestaapi)
[![Supported Versions](https://img.shields.io/pypi/pyversions/wglestaapi)](https://pypi.org/project/wglestaapi)
[![Version](https://img.shields.io/pypi/v/wglestaapi)](https://pypi.org/project/wglestaapi)
[![](https://img.shields.io/pypi/format/wglestaapi)](https://pypi.org/project/wglestaapi)
[![](https://img.shields.io/pypi/wheel/wglestaapi)](https://pypi.org/project/wglestaapi)
[![GitHub Repo stars](https://img.shields.io/github/stars/tankalxat34/wglestaapi?style=social)](https://github.com/tankalxat34/wglestaapi)

Скачивая данную библиотеку вы полностью соглашаетесь со всеми официальными документами **Lesta Games** и **Wargaming.net** об использовании продуктов **Lesta Games** и **Wargaming.net**. *Автор библиотеки (Alexander Podstrechnyy) не несет ответственности за ваши действия, совершенные с помощью данного программного кода.*

## Установка библиотеки

Выполните команду, указанную ниже, в командной строке

```
pip install WgLestaAPI
```

## Пример работы

```py
from WgLestaAPI import Application

# Создание Query с вашим application_id
query = Application.Query(application_id=APP_ID)

# Добавление необходимых параметров
query.extend(search="tank", limit=5)

# Создание метода `account.list` игры Tanks Blitz на RU-регионе с переданными параметрами
m = Application.Method(api_method="account.list", game_shortname="wotb", query=query)

# Выполнение метода
mExecuted = m.execute()

# Ваша обработка ответа от сервера
print(mExecuted['data'][0]['account_id']) # 58114596

# При желании можно перейти по ссылке на официальный сайт от владельца API с документацией
print(m.docs) # https://developers.lesta.ru/reference/all/wotb/account/list/
```

## Функционал библиотеки

В библиотеке реализованы основные функции **API Lesta Games** и **API Wargaming.net**. Все запросы делаются через ваше приложение, которое вы заранее создали на сайте [Lesta Games](https://developers.lesta.ru/applications/) или на сайте [Wargaming.net](https://developers.wargaming.net/applications/). Некоторые функции перечислены ниже:
- Получение информации об игроке, его техники и медалях.
- Получение информации о клане.
- Получение информации о технике, молулях техники.
- и другие методы, не требующие авторизации пользователя.

##  Уведомление об авторских правах

<div style="justify-content: center; text-align: center;">
<img src="https://developers.wargaming.net/static/1.12.2/assets/img/header/wg_logo.png" width="150px" style="margin: 20px;">
<img src="https://developers.lesta.ru/static/1.13.1_lst/assets/img/header/lesta_dev_logo.png" width="178px" style="margin: 20px;">

<caption>API holders</caption>
</div>

- 2022 © Alexander Podstrechnyy. 
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

*Данный программный код не является продуктом Lesta Games и разработан согласно правилам Lesta Games DPP.*

*Данный программный код не является продуктом Wargaming.net и разработан согласно правилам WG DPP.*
# WgLestaAPI

Неофициальная Python библиотека, облегчающая работу с функционалом **API Lesta Games** и **API Wargaming.net** через **Python**. Скачивая данную библиотеку вы полностью соглашаетесь со всеми официальными документами **Lesta Games** и **Wargaming.net** об использовании продуктов **Lesta Games** и **Wargaming.net**. Автор библиотеки (Alexander Podstrechnyy) не несет ответственности за ваши действия, совершенные с помощью данного программного кода.

## Функционал библиотеки

В библиотеке реализованы основные функции **API Lesta Games** и **API Wargaming.net**. Все запросы делаются через ваше приложение, которое вы заранее создали на сайте [Lesta Games](https://developers.lesta.ru/applications/) или на сайте [Wargaming.net](https://developers.wargaming.net/applications/). Некоторые функции перечислены ниже:
- Получение информации об игроке, его техники и медалях.
- Получение информации о клане.
- Получение информации о технике, молулях техники.
- и другие методы, не требующие авторизации пользователя.

##  Уведомление об авторских правах

- 2022 © Alexander Podstrechnyy. Контакты: 
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

# Пример работы

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
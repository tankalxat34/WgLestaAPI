# WgLestaAPI

Unofficial Python library that facilitates working with **API Lesta Games** and **API Wargaming.net** functionality via **Python**. 

[![Downloads](https://static.pepy.tech/personalized-badge/wglestaapi?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads)](https://pepy.tech/project/wglestaapi)
[![Downloads](https://static.pepy.tech/personalized-badge/wglestaapi?period=month&units=international_system&left_color=grey&right_color=blue&left_text=downloads/month)](https://pepy.tech/project/wglestaapi)
[![Downloads](https://static.pepy.tech/personalized-badge/wglestaapi?period=week&units=international_system&left_color=grey&right_color=blue&left_text=downloads/week)](https://pepy.tech/project/wglestaapi)
[![Supported Versions](https://img.shields.io/pypi/pyversions/wglestaapi)](https://pypi.org/project/wglestaapi)
[![Version](https://img.shields.io/pypi/v/wglestaapi)](https://pypi.org/project/wglestaapi)
[![](https://img.shields.io/pypi/format/wglestaapi)](https://pypi.org/project/wglestaapi)
[![](https://img.shields.io/pypi/wheel/wglestaapi)](https://pypi.org/project/wglestaapi)
[![GitHub Repo stars](https://img.shields.io/github/stars/tankalxat34/wglestaapi?style=social)](https://github.com/tankalxat34/wglestaapi)

By downloading this library you fully agree with all official documents **Lesta Games** and **Wargaming.net** about **Lesta Games** and **Wargaming.net** products. *The author of the library (Alexander Podstrechny) is not responsible for your actions performed with the help of this program code.*

## Installing the library

Run the command below at the command line

```
pip install WgLestaAPI
```

## Example of use

```py
from WgLestaAPI import Application

# Creating a Query with your application_id
query = Application.Query(application_id=APP_ID)

# Adding the necessary parameters
query.extend(search="tank", limit=5)

# Creating the method `account.list` of the game Tanks Blitz on the RU-region with the passed parameters
m = Application.Method(api_method="account.list", game_shortname="wotb", query=query)

# Executing the method
mExecuted = m.execute()

# Your server response processing
print(mExecuted['data'][0]['account_id']) # 58114596

# If you wish, you can follow a link to the official website of the API owner with documentation
print(m.docs) # https://developers.lesta.ru/reference/all/wotb/account/list/
```

## Library functionality

The library implements the basic functions of **API Lesta Games** and **API Wargaming.net**. All requests are made through your application, which you previously created on [Lesta Games](https://developers.lesta.ru/applications/) or on [Wargaming.net](https://developers.wargaming.net/applications/). Some features are listed below:
- Getting information about the player, his equipment and medals.
- Obtaining information about the clan.
- Getting information about equipment, equipment mauls.
- And other methods that do not require user authorization.

## Copyright Notice

<div style="justify-content: center; text-align: center;">
<a href="https://developers.wargaming.net/"><img src="https://developers.wargaming.net/static/1.12.2/assets/img/header/wg_logo.png" width="150px" style="margin: 20px;"></a>
<a href="https://developers.lesta.ru/"><img src="https://developers.lesta.ru/static/1.13.1_lst/assets/img/header/lesta_dev_logo.png" width="178px" style="margin: 20px;"></a>
</div>

- 2022 © Alexander Podstrechnyy. 
    - [tankalxat34@gmail.com](mailto:tankalxat34@gmail.com?subject=lestagamesapi)
    - [VKontakte](https://vk.com/tankalxat34)
    - [Telegram](https://tankalxat34.t.me)
    - [GithHub](https://github.com/tankalxat34/wglestaapi)
- 2022 © Wargaming.net. All rights reserved.
    - [User Support Center](http://support.wargaming.net/)
    - [Official website](https://wargaming.net/)
    - [License Agreement](https://eu.wargaming.net/user_agreement/)
    - [Privacy Policy](https://eu.wargaming.net/privacy_policy/)
- 2022 © Lesta Games. All rights reserved. 
    - [User Support Center](https://lesta.ru/support/)
    - [Official website](https://lesta.ru/)
    - [License Agreement](https://developers.lesta.ru/documentation/rules/agreement/)
    - [Privacy Policy](https://legal.lesta.ru/privacy-policy/)

*This program code is not a product of Lesta Games and was developed according to Lesta Games DPP rules.*

*This program code is not a product of Wargaming.net and is developed according to WG DPP rules.*
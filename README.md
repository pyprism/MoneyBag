# MoneyBag [![Build Status](https://travis-ci.org/pyprism/MoneyBag.svg?branch=master)](https://travis-ci.org/pyprism/MoneyBag) [![Coverage Status](https://coveralls.io/repos/github/pyprism/MoneyBag/badge.svg?branch=master)](https://coveralls.io/github/pyprism/MoneyBag?branch=master) [![Requirements Status](https://requires.io/github/pyprism/MoneyBag/requirements.svg?branch=master)](https://requires.io/github/pyprism/MoneyBag/requirements/?branch=master)
:moneybag: Manage honey in your  pocket :moneybag:

This app helps to manage finance according to Chart Of Accounts. All data stored in db encrypted. For encryption its use AES-256!

### Requirements
- Python 3.6
- PostgreSQL
- Web Server (eg: Apache, Nginx)
- OpenSSL Lib ```sudo apt install libssl-dev libffi-dev python3-dev```

### Installation
- Download the [repository](https://github.com/pyprism/MoneyBag/releases/latest) and unzip into your server
- Open and point your terminal to the directory you unzipped MoneyBag
- Run the following commands:
  ```
  virtualenv -p /usr/bin/python3.6 .env
  source .env/bin/activate
  pip install -r requirements.txt
  ./manage.py compress
  cp config.json config.local.json
  
  ```
  - TODO

### Screenshots
<img src="screenshots/dashboard.png">

<a href="https://github.com/pyprism/MoneyBag/tree/master/screenshots">More Screenshots</a>

### Credits
- [Habibur Rahman Shadhin](https://github.com/hrshadhin)
- [Ashutosh Das](https://github.com/pyprism)


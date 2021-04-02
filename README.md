# AQI bot
> ОПИСАНИЕ
## Как поднять проект локально
```bash
foo@bar:~$ git clone https://github.com/Suliko1979/aqi_bishkek_telebot.git
foo@bar:~$ cd qi_bishkek_telebot
foo@bar:~$ cd envs
foo@bar:~$ touch env.local // insert bot token to file
foo@bar:~$ source env.local
foo@bar:~$ python3 -m venv .venv
foo@bar:~$ source .venv/bin/activate
foo@bar:~$ pip install -r requirements/base.txt
foo@bar:~$ python AQI.py
```
## Необходимые программы
- Python 3
- Nginx
- PostgreSQL
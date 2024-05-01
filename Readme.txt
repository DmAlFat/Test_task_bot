-----Установка-----

-Клонировать проект в пустую папку:
git clone https://github.com/DmAlFat/Test_task_bot.git

-Установить необходимые модули:
pip install -r requirements.txt

-Создать файл .env в корне проекта и задать в нём:
* параметры для подключения к Вашей базе данных PostgreSQL (DATABASE,USER,PASSWORD,HOST,PORT):
* TOKEN_API вашего телеграм-бота

-Активировать бота, запустив файл main.py
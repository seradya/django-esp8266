Settings -> Version Control -> Git -> Path
Settings -> Version Control -> Github -> login
VCS -> Checkout from Version Control -> Git

-Создание виртуального окружения
python -m venv espenv

-Запуск виртуального окружения
Settings -> Project Settings -> Project Interpreter

или

cd espenv/scripts
activate.bat
cd..
cd..

-Установка зависимостей
pip install -r requirements.txt

-Запуск сервера
py manage.py runserver

-Отправка изменений
зеленая стрелка VCS

-Отправить
Commit -> Commit and push

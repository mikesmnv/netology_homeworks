Документация по проекту

superuser
username: admin
password: admin1551

Для запуска проекта необходимо:

Провести миграцию:

python manage.py migrate

Загрузить тестовые данные:

python manage.py loaddata fixtures.json

Запустить отладочный веб-сервер проекта:

python manage.py runserver

Проверить выполнение запросов:

test_api_store.http

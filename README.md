# Руководство по запуску
1. В корневой директории создать файл '.env'.
Файл должен содержать:
```
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=

CELERY_BROKER="redis://redis:6379/0"
CELERY_BACKEND="redis://redis:6379/0"

SECRET_KEY=""
ALLOWED_HOSTS="*"
```
2. В терминале выполнить следующую команду:
```
docker compose up --build
```
3. Для запуска тестов выполнить следующие команды:
```
docker exec -it $(docker ps -f name=django -q) bash
python manage.py test
```

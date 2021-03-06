# Хранилище файлов с доступом по HTTP
HTTP API, который предоставляет загрузку (upload), скачивание (download) и удаление файла (delete).
## Что внутри?
Приложение упаковано в Docker-контейнер и разворачивается с помощью docker-compose

Внутри Docker-контейнера доступна команда для запуска приложения:
1. `app` - утилита для запуска приложения

## Как запустить локально с Docker?
1. Создать в папке `deploy` скрытый файл `.env.prod`
2. Заполнить данные на примере файла `.env.test`
3. Выполнить команду `make run` в терминале в корневой директории проекта
4. Для остановки контейнеров используйте `make stop`, для удаления `make down`.

## Как запустить локально без Docker?
Создание и активация виртуального окружения
```
python3.10 -m venv venv
source venv/bin/activate
```
Активация переменных окружения
```
export $(grep -v '^#' deploy/.env.test | xargs)
```
Установка приложения через `pip` и запуск приложения
```
pip install -e .
app
```
Проверка работоспособности
```
curl localhost:8080/ping/app
```

## Разработка
### Быстрые команды
- `make run` Запуск контейнеров
- `make build` Пересборка контейнеров при изменениях в коде
- `make stop` Остановка контейнеров
- `make down` Остановка и удаление контейнеров
- `make lint` Запуск линтера flake8
- `make cs` Запуск black для форматирования кода 
- `make test` Запуск тестов
- `make test-cov` Запуск тестов с покрытием кода
- `make test-cov-html` Запуск тестов с отчетом в html
- `make req` Обновление зависимостей
### Документация
- `localhost:8080/docs`
- `localhost:8080/redoc`

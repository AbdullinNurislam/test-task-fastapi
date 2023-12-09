## Сервис для сбора перформанс метрик сервисов ##

### Формулировка задачи ###

Необходимо реализовать минимальное апи для добавления 
и анализа метрик производительности с различных сервисов.

[Полная формулировка тестового задания](TASK.md)

---
### Зависимости ###

* docker, docker compose
* make
* python 3.10^ (только для запуска вне docker контейнера)
* poetry (только для запуска вне docker контейнера)

Проект реализован с использованием ОС Ubuntu 22.04

---
### Установка и запуск проекта ###

1. Клонируем проект и переходим в его директорию для дальнейшей работы:
    - `git clone https://github.com/AbdullinNurislam/test-task-fastapi`
    - `cd test-task-fastapi`

2. Настройка переменных окружения.
  Создаём .env файл, с нужными переменными окружения.
  Все необходимые энвы для примера имеются в файле .env.sample,
  поэтому можно сделать с него копию:
    - `make init`

3. Собираем docker-образ приложения:
  - `make build`

4. Запускаем контейнер с СУБД:
  - `make db`

5. Применяем миграции:
  - `make alembic`

6. запускаем приложение:
  - `make app`

---
### Разработка проекта ###

1. Для разработки необходимо:
  * 1.1. Установить Python3.10 или новее
  * 1.2. Установить менеджер пакетов [poetry](https://python-poetry.org/)
  * 1.3. Установить зависимости проекта с помощью poetry:
    - `poetry install`
  * 1.4. активировать окружение проекта:
    - `poetry shell`
2. Для работы с `alembic` необходимо перейти в папку `src` и указывать перед командой 
  переменную окружения `DATABASE_URL`. 
  Примеры команд `alembic` для работы с БД, запущенной с параметрами, указанными в `.env.sample`:
    - `DATABASE_URL=postgresql+asyncpg://postgres_test:postgres_test@127.0.0.1:5434/postgres_test 
    alembic current`
    - `DATABASE_URL=postgresql+asyncpg://postgres_test:postgres_test@127.0.0.1:5434/postgres_test 
    alembic revision --autogenerate -m "migration_name"`
    - `DATABASE_URL=postgresql+asyncpg://postgres_test:postgres_test@127.0.0.1:5434/postgres_test 
    alembic history"`
    - `DATABASE_URL=postgresql+asyncpg://postgres_test:postgres_test@127.0.0.1:5434/postgres_test 
    alembic upgrade head"`

### TODO ###

- [ ] Добавить тесты эндпоинтов
- [ ] Добавить пагинацию в эндпоинт `GET /metrics/<service-name: str>`
- [x] README.md
- [ ] Добавить тесты применения миграций (например, с созданием тестовой БД)
- [ ] Добавить в эндпоинт получения метрик возможность фильтрации за период
- [ ] рефакторинг

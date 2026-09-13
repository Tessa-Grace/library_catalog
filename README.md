# Library Catalog API - Учебный проект FastAPI

Реализация REST API для библиотечного каталога с правильной архитектурой, которая демонстрирует все best practices разработки на FastAPI.

## Технологии
1. FastAPI
2. Uvicorn
3. PostgreSQL
4. SQLAlchemy
5. Alembic
6. Pydantic
7. httpx
8. Poetry

## REST API для управления библиотечным каталогом с функциями:
- CRUD операции с книгами
- Поиск и фильтрация
- Автоматическое обогащение данных из Open Library
- Хранение в PostgreSQL
- Пагинация результатов
- Обработка ошибок

## Как запустить проект:
1. Клонировать репозиторий
```
git clone https://github.com/Tessa-Grace/library_catalog.git
```
```
cd library_catalog
```

3. Установить зависимости
```
poetry install
```

4. Создать .env файл
```
cp .env.example .env
```

5. Запустить PostgreSQL
```
docker-compose up -d postgres
```

6. Применить миграции
```
poetry run alembic upgrade head
```

7. Запустить приложение
```
poetry run uvicorn src.library_catalog.main:app --reload
```

Приложение будет доступно по адресу: http://localhost:8000

## Документация API
Примеры запросов к API и их описание доступны в документации Swagger по адресу: http://localhost:8000/docs.

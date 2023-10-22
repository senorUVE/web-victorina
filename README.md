# FastAPI & PostgreSQL Service

Сервис, разработанный на основе FastAPI, предназначенный для взаимодействия с базой данных PostgreSQL. Это руководство поможет всем вам развернуть и использовать данный сервис с использованием Docker и Docker Compose.

## Оглавление

- [Подготовка](#подготовка)
- [Развертывание PostgreSQL](#развертывание-postgresql)
- [Сборка и запуск FastAPI сервиса](#сборка-и-запуск-fastapi-сервиса)
- [Примеры использования](#примеры-использования)

---

## Подготовка

1. Убедитесь, что у вас установлены Docker и Docker Compose.
2. Клонируйте данный репозиторий на ваш локальный компьютер:

```bash
git clone [URL репозитория]
cd [имя директории репозитория]
```
## Развертывание PostgreSQL
Запустите PostgreSQL с помощью Docker Compose:
```bash
docker-compose up -d postgres
```
Это создаст контейнер с PostgreSQL, доступный по порту 5432.
## Сборка и запуск FastAPI сервиса
Соберите Docker-образ для FastAPI сервиса:
```bash
docker build -t fastapi-service:latest .
```
Запустите сервис с помощью Docker Compose:
```bash
docker-compose up -d fastapi-service
```
Теперь FastAPI сервис будет доступен на порту 8000.
## Примеры использования
Для получения вопросов из публичного API и их сохранения в базе данных PostgreSQL, выполните следующий запрос:
```
bash
curl -X POST "http://localhost:8000/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"questions_num":1}'
```


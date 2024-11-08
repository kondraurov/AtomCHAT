# AtomCHAT

Проект представляет собой чат в реальном времени с использованием FastAPI для API, SQLAlchemy для взаимодействия с БД.


## Стек технологий:

Backend: FastAPI

Frontend: HTML, JavaScript, CSS 

ORM: SQLAlchemy

База данных: SQLite

Реализация отправки сообщений в реальном времени: WebSocket

## Список реализованного функционала:

1) Регистрация новых пользователей и авторизация;
2) Предусмотрена роль модератора, которому доступны все каналы по энд-поинту /chat/all_dialogues и предоставлена возможность блокировки пользователей по энд-поинту /auth/block (доступ к этим функциям есть только у модераторов);
3) Сообщения отправляются в режиме реального времени;
4) Пользователям доступен функционал просмотра истории сообщений;
5) Приложение запускается через docker-compose;
6) Создан скрипт для создания тестовых данных (создаются пользователи Михаил и Дарья, которые отправляют друг другу два сообщения). Скрипт находится в корневой папке проекта:

```
C:\Users\KOVALEV\PycharmProjects\AtomCHAT
```

Для проверки функций, доступных модератору, можно воспользоваться этим аккаунтом:

***email:*** test@mail.ru

***password:*** test0000

## Инструкция по запуску решения:

### 1) Клонируйте репозиторий.

### 2) Создайте виртуальное окружение:

```
python -m venv venv
```
### 3) Активируйте виртуальное окружение:

```
.\venv\Scripts\activate
```

### 4) Установите зависимости:

```
pip install -r requirements.txt
```

### 5) Запустите скрипт для создания тестовых данных.

Скрипт по созданию тестовых данных запускается из корневой директории.

Тестовый скрипт необходимо запустить до запуска решения, прописав в терминале следующую команду:

```
python -m app.create_test_data create
```

Для удаления тестовых данных необходимо прописать:

```
python -m app.create_test_data delete
```

### 6) Пропишите в терминал следующую команду:

```
docker-compose up --build
```

В этот момент у вас должен собраться docker-образ и создаться контейнер с портом 8000, который позволит увидеть решение.
import sys
import asyncio
from sqlalchemy import delete, select
from app.database import async_session_maker
from app.users.models import User
from app.chat.models import Message
from app.users.auth import get_password_hash



# Функция для создания тестовых пользователей
async def create_test_users():
    async with async_session_maker() as session:
        test_users = [
            {"name": "Михаил", "email": "misha@example.com", "hashed_password": get_password_hash("password1")},
            {"name": "Дарья", "email": "dasha@example.com", "hashed_password": get_password_hash("password2")},
        ]

        for user_data in test_users:
            user = User(**user_data, is_test=True)
            session.add(user)

        await session.commit()


# Функция для создания тестовых сообщений
async def create_test_messages():
    async with async_session_maker() as session:
        # Получаем тестовых пользователей для создания сообщений
        test_user1 = await session.scalar(select(User).where(User.email == "misha@example.com"))
        test_user2 = await session.scalar(select(User).where(User.email == "dasha@example.com"))

        if test_user1 and test_user2:
            test_messages = [
                {"sender_id": test_user1.id, "recipient_id": test_user2.id, "content": "Привет от Михаила!", "is_test": True},
                {"sender_id": test_user2.id, "recipient_id": test_user1.id, "content": "Привет от Дарьи!", "is_test": True},
            ]

            for msg_data in test_messages:
                message = Message(**msg_data)
                session.add(message)

            await session.commit()


# Функция для удаления всех тестовых данных (только тестовые пользователи и сообщения)
async def delete_test_data():
    async with async_session_maker() as session:
        # Удаляем тестовые сообщения
        await session.execute(delete(Message).where(Message.is_test == True))
        # Удаляем тестовых пользователей
        await session.execute(delete(User).where(User.is_test == True))
        await session.commit()


# Главная функция для обработки командной строки
async def main():
    if len(sys.argv) < 2:
        print("Укажите команду: create или delete")
        return

    action = sys.argv[1].lower()

    if action == "create":
        await create_test_users()
        await create_test_messages()
        print("Тестовые данные созданы.")
    elif action == "delete":
        await delete_test_data()
        print("Тестовые данные удалены.")
    else:
        print("Неизвестная команда. Используйте 'create' или 'delete'.")


# Запуск main() с помощью asyncio
if __name__ == "__main__":
    asyncio.run(main())

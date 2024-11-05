from sqlalchemy import String, Integer, text, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)

    is_user: Mapped[bool] = mapped_column(default=True, server_default=text('true'), nullable=False)
    is_moderator: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_blocked: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_test: Mapped[bool] = mapped_column(Boolean, default=False, server_default=text('false'), nullable=False)
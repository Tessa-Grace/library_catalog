import uuid
from datetime import datetime

from sqlalchemy import JSON, Boolean, DateTime, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from ...core.database import Base


class Book(Base):
    """
    Модель книги в библиотечной системе.
    
    Эта модель представляет книгу со всей необходимой информацией:
    - Основные метаданные (название, автор, год, жанр)
    - Физические характеристики (количество страниц)
    - Статус доступности
    - Уникальные идентификаторы (ISBN, внутренний ID)
    
    Аттрибуты:
        book_id (UUID): Уникальный идентификатор книги
        title (str): Название книги (до 500 символов)
        author (str): Автор книги (до 300 символов)
        year (int): Год издания
        genre (str): Жанр книги
        pages (int): Количество страниц
        available (bool): Доступна ли книга для выдачи
        isbn (str/None): Международный стандартный номер книги
        description (str | None): Описание книги
        extra (dict | None): Дополнительные данные
        created_at (datetime): Дата создания записи
        updated_at (datetime): Дата последнего обновления
    """
    __tablename__ = "books"
    
    book_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    
    title: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        index=True,
    )

    author: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
        index=True,
    )

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        index=True,
    )

    genre: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    pages: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    available: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        index=True,
    )

    isbn: Mapped[str | None] = mapped_column(
        String(20),
        unique=True,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    extra: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<Book(id={self.book_id}, title='{self.title}')>"

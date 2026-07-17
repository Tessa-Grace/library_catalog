import uuid
from datetime import datetime
from sqlalchemy import Boolean, DateTime, Integer, JSON, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from ...core.database import Base

class Book(Base):
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
    
    # ... остальные поля
    author: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
        index=True,
    )

    year: Mapped[int] = mapped_column(
        nullable=False,
        index=True,
    )

    genre: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    pages: Mapped[int] = mapped_column(
        nullable=False,
    )

    available: Mapped[bool] = mapped_column(
        default=True,
        index=True,
    )
# добавить:
# докстринги
# и
# **Timestamps:**
# - `created_at: datetime` - автоматически при создании
# - `updated_at: datetime` - автоматически при обновлении

    def __repr__(self) -> str:
        return f"<Book(id={self.book_id}, title='{self.title}')>"
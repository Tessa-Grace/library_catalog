from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class BookCreateDTO(BaseModel):
    """
    DTO для создания книги.
    
    Используется в BookService.create_book().
    """
    title: str
    author: str
    year: int
    genre: str
    pages: int
    isbn: str | None = None
    description: str | None = None


class BookUpdateDTO(BaseModel):
    """
    DTO для обновления книги.
    
    Все поля опциональны — обновляются только переданные.
    """
    title: str | None = None
    author: str | None = None
    year: int | None = None
    genre: str | None = None
    pages: int | None = None
    available: bool | None = None
    isbn: str | None = None
    description: str | None = None


class BookDTO(BaseModel):
    """
    DTO книги для домена.
    
    Возвращается из BookService.
    """
    book_id: UUID
    title: str
    author: str
    year: int
    genre: str
    pages: int
    available: bool
    isbn: str | None
    description: str | None
    extra: dict | None
    created_at: datetime
    updated_at: datetime
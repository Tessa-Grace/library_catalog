from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.book import Book
from .base_repository import BaseRepository


class BookRepository(BaseRepository[Book]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Book)
    
    async def find_by_filters(
        self,
        title: str | None = None,
        author: str | None = None,
        genre: str | None = None,
        year: int | None = None,
        available: bool | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> list[Book]:
        """Поиск книг с фильтрацией."""
        res = select(self.model)
        
        if title:
            res = res.where(self.model.title.ilike(f"%{title}%"))
        if author:
            res = res.where(self.model.author.ilike(f"%{author}%"))
        if genre:
            res = res.where(self.model.genre == genre)
        if year:
            res = res.where(self.model.year == year)
        if available is not None:
            res = res.where(self.model.available == available)
        
        res = res.limit(limit).offset(offset)
        result = await self.session.execute(res)
        return list(result.scalars().all())

    
    async def find_by_isbn(self, isbn: str) -> Book | None:
        """Найти книгу по ISBN."""
        res = select(self.model).where(self.model.isbn == isbn)
        result = await self.session.execute(res)
        return result.scalars().first()
    
    async def count_by_filters(
        self,
        title: str | None = None,
        author: str | None = None,
        genre: str | None = None,
        year: int | None = None,
        available: bool | None = None,
    ) -> int:
        """Подсчитать количество книг по фильтрам."""
        res = select(func.count()).select_from(self.model)
        
        if title:
            res = res.where(self.model.title.ilike(f"%{title}%"))
        if author:
            res = res.where(self.model.author.ilike(f"%{author}%"))
        if genre:
            res = res.where(self.model.genre == genre)
        if year:
            res = res.where(self.model.year == year)
        if available is not None:
            res = res.where(self.model.available == available)
        
        result = await self.session.execute(res)
        return result.scalar() or 0

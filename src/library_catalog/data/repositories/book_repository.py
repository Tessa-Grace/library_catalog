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
        pass
    
    async def find_by_isbn(self, isbn: str) -> Book | None:
        """Найти книгу по ISBN."""
        pass
    
    async def count_by_filters(
        self,
        title: str | None = None,
        author: str | None = None,
        # ... остальные фильтры
    ) -> int:
        """Подсчитать количество книг по фильтрам."""
        pass
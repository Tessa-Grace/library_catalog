from ...data.models.book import Book
from ..schemas.book import BookDTO


class BookMapper:
    """Маппер для преобразования ORM-модели Book в Domain DTO."""
    
    @staticmethod
    def to_book_dto(book: Book) -> BookDTO:
        """Преобразовать Book ORM модель в BookDTO."""
        return BookDTO(
            book_id=book.book_id,
            title=book.title,
            author=book.author,
            year=book.year,
            genre=book.genre,
            pages=book.pages,
            available=book.available,
            isbn=book.isbn,
            description=book.description,
            extra=book.extra,
            created_at=book.created_at,
            updated_at=book.updated_at,
        )
    
    @staticmethod
    def to_book_dtos(books: list[Book]) -> list[BookDTO]:
        """Преобразовать список ORM-моделей в список DTO."""
        return [BookMapper.to_book_dto(book) for book in books]


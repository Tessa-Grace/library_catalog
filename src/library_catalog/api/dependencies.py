import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, Request, Security, status
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.config import settings
from ..core.database import get_db
from ..data.repositories.book_repository import BookRepository
from ..domain.services.book_service import BookService
from ..external.openlibrary.client import OpenLibraryClient

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# ========== EXTERNAL CLIENTS (Singletons) ==========

def get_openlibrary_client(request: Request) -> OpenLibraryClient:
    """
    Получить OpenLibraryClient из app.state.
    
    Клиент создаётся один раз в lifespan и хранится в app.state.
    """
    return request.app.state.openlibrary_client


# ========== REPOSITORIES ==========

async def get_book_repository(
    db: Annotated[AsyncSession, Depends(get_db)]
) -> BookRepository:
    """
    Создать BookRepository для текущей сессии БД.
    
    Создается новый экземпляр для каждого запроса.
    """
    return BookRepository(db)


# ========== SERVICES ==========

async def get_book_service(
    book_repo: Annotated[BookRepository, Depends(get_book_repository)],
    ol_client: Annotated[OpenLibraryClient, Depends(get_openlibrary_client)],
) -> BookService:
    """
    Создать BookService с внедренными зависимостями.
    
    FastAPI автоматически разрешит все зависимости:
    1. get_db() создаст AsyncSession
    2. get_book_repository() создаст BookRepository с session
    3. get_openlibrary_client() вернет singleton клиент
    4. Все внедрится в BookService
    """
    return BookService(
        book_repository=book_repo,
        openlibrary_client=ol_client,
    )


# ========== TYPE ALIASES ДЛЯ УДОБСТВА ==========

# Можно использовать в роутерах так:
# async def my_route(service: BookServiceDep):
BookServiceDep = Annotated[BookService, Depends(get_book_service)]
BookRepoDep = Annotated[BookRepository, Depends(get_book_repository)]
DbSessionDep = Annotated[AsyncSession, Depends(get_db)]


async def verify_api_key(
    api_key: Annotated[str | None, Security(api_key_header)],
) -> None:
    """Проверить API-ключ из заголовка X-API-Key."""
    if api_key is None or not secrets.compare_digest(
        api_key.encode(), settings.api_key.encode()
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )


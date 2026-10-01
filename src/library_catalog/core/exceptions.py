import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from ..api.middleware import request_id_var

logger = logging.getLogger(__name__) 

class AppException(Exception):
    """Базовое исключение приложения."""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class NotFoundException(AppException):
    """Ресурс не найден."""
    def __init__(self, resource: str, identifier: any):
        super().__init__(
            message=f"{resource} with id '{identifier}' not found",
            status_code=404,
        )

def register_exception_handlers(app: FastAPI) -> None:
    """Зарегистрировать обработчики исключений."""
    
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message},
        )
    
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        """Обработчик непредвиденных исключений."""
        
        logger.error(
            f"Unhandled exception: {exc}",
            exc_info=True,
            extra={
                "path": request.url.path,
                "method": request.method,
                "request_id": request_id_var.get() or "-",
            },
        )
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"},
        )

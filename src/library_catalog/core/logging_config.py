import logging

from ..api.middleware import request_id_var


class RequestIDFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_var.get() or "-"
        return True

    def setup_logging() -> None:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - [%(request_id)s] - %(message)s"
        )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.addFilter(RequestIDFilter())

        root = logging.getLogger()
        root.setLevel(logging.INFO)
        root.handlers.clear()  # убираем старые
        root.addHandler(handler)

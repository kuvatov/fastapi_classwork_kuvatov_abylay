from typing import Any

from fastapi.exceptions import HTTPException


class BaseHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: Any = None, headers: dict[str, str] | None = None) -> None:
        if not headers:
            headers = {"WWW-Authenticate": "Bearer"}

        super().__init__(status_code, detail, headers)


class HTTPBadRequestException(BaseHTTPException):
    def __init__(self, status_code: int, detail: Any = None, headers: dict[str, str] | None = None) -> None:
        super().__init__(400, detail, headers)


class HTTPNotFoundException(BaseHTTPException):
    def __init__(self, status_code: int, detail: Any = None, headers: dict[str, str] | None = None) -> None:
        super().__init__(404, detail, headers)
        
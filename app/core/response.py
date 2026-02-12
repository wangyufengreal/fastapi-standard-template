from typing import Any, Generic, TypeVar, cast

from pydantic import BaseModel

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    code: int
    message: str
    data: T | None = None

    @classmethod
    def success(cls, data: T | None = None, message: str = "success") -> dict[str, Any]:
        return cast(
            dict[str, Any],
            cls(code=0, message=message, data=data).model_dump(),
        )

    @classmethod
    def error(cls, code: int, message: str) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            cls(code=code, message=message, data=None).model_dump(),
        )

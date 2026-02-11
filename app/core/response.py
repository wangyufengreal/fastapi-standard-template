from typing import TypeVar, Generic, Optional, Dict

from pydantic import BaseModel


T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    code: int
    message: str
    data: Optional[T] = None

    @classmethod
    def success(cls, data: T = None, message: str = "success") -> Dict:
        return cls(code=0, message=message, data=data).model_dump()
    
    @classmethod
    def error(cls, code: int, message: str) -> Dict:
        return cls(code=code, message=message, data=None).model_dump()

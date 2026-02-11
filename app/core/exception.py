from typing import Optional

from app.core.error_code import ErrorCode


class AppException(Exception):
    def __init__(
        self, 
        code: ErrorCode, 
        message: Optional[str] = None,
    ):
        self.code = code.code
        self.message = message or code.message
        super().__init__(message)


class ParamError(AppException):
    def __init__(self, message: str = None):
        super().__init__(ErrorCode.PARAM_ERROR, message)


class ValidationError(AppException):
    def __init__(self, message: str = None):
        super().__init__(ErrorCode.VALIDATION_ERROR, message)


class BussinessError(AppException):
    def __init__(self, message: str = None):
        super().__init__(ErrorCode.BUSINESS_ERROR, message)


class UnanthorizedException(AppException):
    def __init__(self, message: str = None):
        super().__init__(ErrorCode.UNAUTHORIZED, message)

class ForbiddenException(AppException):
    def __init__(self, message: str = None):
        super().__init__(ErrorCode.FORBIDDEN, message)

class SystemError(AppException):
    def __init__(self, message: str = None):
        super().__init__(ErrorCode.SYSTEM_ERROR, message)

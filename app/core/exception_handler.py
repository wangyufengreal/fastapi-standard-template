import structlog
from structlog.stdlib import BoundLogger
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from app.core.error_code import ErrorCode
from app.core.exception import (
    AppException, ParamError, ValidationError, 
    BussinessError, UnanthorizedException, 
    ForbiddenException, SystemError)
from app.core.response import ResponseModel


logger: BoundLogger = structlog.get_logger()

async def app_exception_handler(request: Request, exc: AppException):
    logger.warning(
        f"应用异常: code='{exc.code}', message='{exc.message}', path={request.url.path}"
    )
    return JSONResponse(
        status_code=200,
        content=ResponseModel.error(
            code=exc.code,
            message=exc.message,
        ),
    )

async def global_exception_handler(request: Request, _: Exception):
    logger.exception(
        f"未捕获的异常: path='{request.url.path}'"
    )
    return JSONResponse(
        status_code=500,
        content=ResponseModel.error(
            code=ErrorCode.SYSTEM_ERROR.code, 
            message=ErrorCode.SYSTEM_ERROR.message,
        ),
    )

def init_exception_handlers(app: FastAPI):
    business_exceptions = [
        AppException, ParamError, ValidationError, BussinessError,
        UnanthorizedException, ForbiddenException, SystemError
    ]
    for exc in business_exceptions:
        app.add_exception_handler(exc, app_exception_handler)

    app.add_exception_handler(Exception, global_exception_handler)

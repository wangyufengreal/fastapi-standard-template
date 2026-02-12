import time

import structlog
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from structlog.stdlib import BoundLogger

from app.core.log_context import request_id_ctx

logger: BoundLogger = structlog.get_logger()


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id_ctx.set(None)
        start = time.perf_counter()

        try:
            response = await call_next(request)
            latency = int((time.perf_counter() - start) * 1000)

            logger.info(
                "请求完成",
                method=request.method,
                path=request.url.path,
                status_code=response.status_code,
                latency_ms=latency,
            )
            return response

        except Exception:
            logger.exception(
                "请求失败",
                method=request.method,
                path=request.url.path,
            )
            raise

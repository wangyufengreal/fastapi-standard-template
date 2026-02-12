"""
FastAPI 应用主入口文件

此模块创建了一个最小化的 FastAPI 应用，包含根路径和健康检查端点。
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.core.config import get_settings
from app.core.exception_handler import init_exception_handlers
from app.core.logging import configure_logging
from app.core.middleware import LoggingMiddleware
from app.core.response import ResponseModel

configure_logging()

settings = get_settings()


# 创建 FastAPI 应用实例
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    debug=settings.DEBUG,
)
app.add_middleware(LoggingMiddleware)

# 初始化异常处理
init_exception_handlers(app)


@app.get("/", response_model=ResponseModel[str])
async def read_root() -> dict[str, str]:
    """
    根路径端点

    返回:
        Dict[str, str]: 包含欢迎消息的字典
    """
    return ResponseModel.success(data="欢迎使用 FastAPI 标准模板")


@app.get("/health", response_model=ResponseModel[str])
async def health_check() -> JSONResponse:
    """
    健康检查端点

    返回:
        JSONResponse: 包含应用健康状态的 JSON 响应
    """
    return ResponseModel.success(data="服务工作正常")

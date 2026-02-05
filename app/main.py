"""
FastAPI 应用主入口文件

此模块创建了一个最小化的 FastAPI 应用，包含根路径和健康检查端点。
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict

# 创建 FastAPI 应用实例
app = FastAPI(
    title="FastAPI Standard Template",
    description="一个符合最佳实践的 FastAPI 应用模板",
    version="1.0.0",
)


@app.get("/")
async def read_root() -> Dict[str, str]:
    """
    根路径端点
    
    返回:
        Dict[str, str]: 包含欢迎消息的字典
    """
    return {"message": "欢迎使用 FastAPI 标准模板"}


@app.get("/health")
async def health_check() -> JSONResponse:
    """
    健康检查端点
    
    返回:
        JSONResponse: 包含应用健康状态的 JSON 响应
    """
    health_status = {
        "status": "healthy",
        "service": "fastapi-template",
        "version": "1.0.0",
        "timestamp": "2026-02-05T06:13:25Z"
    }
    return JSONResponse(content=health_status)

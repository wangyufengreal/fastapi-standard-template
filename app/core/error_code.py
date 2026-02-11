from enum import Enum


class ErrorCode(Enum):
    """
    错误码设计

    0: 成功
    1xxxx: 参数/校验错误
    2xxxx: 业务逻辑错误
    3xxxx: 权限/认证错误
    4xxxx: 资源错误
    5xxxx: 系统/内部错误
    """
    SUCCESS = (0, "请求成功")
    
    # ===== 参数/校验错误 =====
    PARAM_ERROR = (10001, "参数错误")
    VALIDATION_ERROR = (10002, "参数校验失败")

    # ===== 业务逻辑错误 =====
    BUSINESS_ERROR = (20001, "业务处理失败")

    # ===== 权限错误 =====
    UNAUTHORIZED = (30001, "未登录或登录已过期")
    FORBIDDEN = (30002, "无访问权限")

    # ===== 系统错误 =====
    SYSTEM_ERROR = (50000, "系统内部错误")

    @property
    def code(self) -> int:
        return self.value[0]
    
    @property
    def message(self) -> str:
        return self.value[1]

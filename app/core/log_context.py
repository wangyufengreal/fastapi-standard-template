import uuid
from contextvars import ContextVar

request_id_ctx: ContextVar[str | None] = ContextVar("request_id", default=None)


def get_request_id() -> str | None:
    rid: str | None = request_id_ctx.get()
    if rid is None:
        rid = uuid.uuid4().hex
        request_id_ctx.set(rid)
    return rid

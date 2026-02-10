import contextvars
import uuid

request_id_ctx = contextvars.ContextVar("request_id", default=None)

def get_request_id() -> str:
    rid = request_id_ctx.get()
    if rid is None:
        rid = uuid.uuid4().hex
        request_id_ctx.set(rid)
    return rid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


import logging



class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        body_bytes = await request.body()
        try:
            body = body_bytes.decode("utf-8")
        except Exception:
            body = str(body_bytes)
        
        response = await call_next(request)
        if response.status_code != 307:
            logging.info(f"Request: {request.method} {request.url} Body: {body}")
            logging.info(f"Response status: {response.status_code}")
        return response
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from src.modules.domain.enum.log_enums import LogLevel
from src.modules.service.logging.logger.service.logger_service import LoggerService


class ConnectionLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)
        client_ip = request.client.host
        route = request.url.path
        method = request.method
        response_code = response.status_code
        message = f"{client_ip} - {route} - {method} - {response_code}"
        LoggerService.send_log(LogLevel.INFO, message)
        return response

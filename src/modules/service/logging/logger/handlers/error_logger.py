import datetime

from src.modules.domain.enum.log_enums import LogLevel
from src.modules.service.logging.logger.handlers.abstract_logger import AbstractLogger
from src.modules.service.logging.logger.service.logger_service import LoggerService


class ErrorLogger(AbstractLogger):
    log_level = LogLevel.INFO

    def log(self, message) -> bool:
        if not message:
            LoggerService.send_log(LogLevel.WARNING, "Attempt to crete empty log")
            return False
        new_message = f"[{datetime.datetime.utcnow()}] ERROR {message}"
        self.write_log(new_message)
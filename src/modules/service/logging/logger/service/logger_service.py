from src.modules.domain.enum.log_enums import LogLevel
from src.modules.service.logging.logger.handlers.abstract_logger import AbstractLogger
from src.modules.service.managers.settings_manager import SettingsManager


class LoggerService:
    loggers = []

    @staticmethod
    def register_logger(logger: AbstractLogger):
        if logger is None or not isinstance(logger, AbstractLogger) or logger in LoggerService.loggers:
            return
        LoggerService.loggers.append(logger)

    @staticmethod
    def send_log(log_level: LogLevel, message: str):
        if SettingsManager().settings.log_level >= log_level.value:
            for i in LoggerService.loggers:
                if i.log_level == log_level:
                    i.log(message)
                    return

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(LoggerService, cls).__new__(cls)
        return cls.instance

from src.modules.service.logging.logger.handlers.abstract_logger import AbstractLogger
from src.modules.service.logging.logger.service.logger_service import LoggerService
from src.modules.service.logging.logger.handlers.info_logger import InfoLogger
from src.modules.service.logging.logger.handlers.warning_logger import WarningLogger
from src.modules.service.logging.logger.handlers.debug_logger import DebugLogger
from src.modules.service.logging.logger.handlers.error_logger import ErrorLogger


class LoggerInitializer:

    @staticmethod
    def initialize_loggers():
        inh_children = AbstractLogger.__subclasses__()
        for i in inh_children:
            instance = i()
            LoggerService.register_logger(instance)

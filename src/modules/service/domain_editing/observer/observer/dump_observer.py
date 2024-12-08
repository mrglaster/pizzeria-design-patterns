from src.modules.domain.enum.log_enums import LogLevel
from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.service.domain_editing.observer.observer.abstract_observer import AbstractObserverHandler
from src.modules.factory.repository_factory.repository_factory import RepositoryFactory
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService
from src.modules.service.logging.logger.service.logger_service import LoggerService


class DumpObserverHandler(AbstractObserverHandler):
    __event_type = ObservableActionType.ACTION_DUMP

    def __init__(self):
        super().__init__()
        self.repository_factory = RepositoryFactory()
        ObserverService.register_observer(self)

    @property
    def event_type(self):
        return self.__event_type

    def notify(self, obj, *args) -> bool:
        LoggerService.send_log(LogLevel.INFO, "Creating database dump")
        try:
            repos = self.repository_factory.repositories.values()
            for i in repos:
                instance = i()
                instance.dump()
            LoggerService.send_log(LogLevel.INFO, "Database dump has been created successfully")
            return True
        except Exception as e:
            LoggerService.send_log(LogLevel.ERROR, f"Unable to create database dump: {e}")
            return False

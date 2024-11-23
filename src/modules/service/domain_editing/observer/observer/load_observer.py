from src.modules.domain.enum.log_enums import LogLevel
from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.factory.repository_factory.repository_factory import RepositoryFactory
from src.modules.service.domain_editing.observer.observer.abstract_observer import AbstractObserverHandler
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService
from src.modules.service.logging.logger.service.logger_service import LoggerService


class LoadObserverHandler(AbstractObserverHandler):
    __event_type = ObservableActionType.ACTION_LOAD_DUMP

    def __init__(self):
        super().__init__()
        self.repository_factory = RepositoryFactory()
        ObserverService.register_observer(self)

    @property
    def event_type(self):
        return self.__event_type

    def notify(self, obj, *args) -> bool:
        try:
            LoggerService.send_log(LogLevel.INFO, "Loading database from dump")
            repos = self.repository_factory.repositories.values()
            for i in repos:
                instance = i()
                instance.load_dump(clear_repository=True)
            LoggerService.send_log(LogLevel.INFO, "Database has been successfully laoded from the dump")
            return True
        except Exception as e:
            LoggerService.send_log(LogLevel.INFO, f"Unable to load database from dump: {e}")
            return False

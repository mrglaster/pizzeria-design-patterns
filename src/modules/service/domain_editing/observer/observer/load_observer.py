from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.factory.repository_factory.repository_factory import RepositoryFactory
from src.modules.service.domain_editing.observer.observer.abstract_observer import AbstractObserverHandler
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService


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
            repos = self.repository_factory.repositories.values()
            for i in repos:
                instance = i()
                instance.load_dump(clear_repository=True)
            return True
        except:
            return False

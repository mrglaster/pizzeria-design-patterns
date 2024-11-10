from src.modules.service.domain_editing.observer.observer.abstract_observer import AbstractObserver
from src.modules.service.domain_editing.observer.observer.create_observer import CreateObserver
from src.modules.service.domain_editing.observer.observer.delete_observer import DeleteObserver
from src.modules.service.domain_editing.observer.observer.update_observer import UpdateObserver
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService


class ObserverInitializer:

    @staticmethod
    def initialize_observers():
        inh_children = AbstractObserver.__subclasses__()
        for i in inh_children:
            instance = i()
            ObserverService.register_observer(instance)


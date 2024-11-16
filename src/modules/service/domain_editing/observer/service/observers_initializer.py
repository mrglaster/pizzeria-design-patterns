from src.modules.service.domain_editing.observer.observer.abstract_observer import AbstractObserverHandler
from src.modules.service.domain_editing.observer.observer.create_observer import CreateObserverHandler
from src.modules.service.domain_editing.observer.observer.delete_observer import DeleteObserverHandler
from src.modules.service.domain_editing.observer.observer.update_observer import UpdateObserverHandler
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService


class ObserverInitializer:

    @staticmethod
    def initialize_observers():
        inh_children = AbstractObserverHandler.__subclasses__()
        for i in inh_children:
            instance = i()
            ObserverService.register_observer(instance)


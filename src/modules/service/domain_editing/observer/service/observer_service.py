from src.modules.service.domain_editing.domain_editing_service.crud_service import AbstractCrudService
from src.modules.service.domain_editing.observer.observer.abstract_observer import AbstractObserver


class ObserverService:
    observers = []

    @staticmethod
    def register_observer(service: AbstractObserver):
        if service is None or not isinstance(service, AbstractObserver):
            return
        items = list(map(lambda x: type(x).__name__, ObserverService.observers))
        found = type(service).__name__ in items
        if not found:
            ObserverService.observers.append(service)

    @staticmethod
    def raise_event(event_type, item, *args):
        for observer_instance in ObserverService.observers:
            if observer_instance.event_type == event_type:
                return observer_instance.notify(item, args)
        return False

from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.service.domain_editing.observer.observer.abstract_observer import AbstractObserver
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService
from src.modules.service.domain_editing.post_processing.post_processor import PostProcessor


class UpdateObserver(AbstractObserver):
    __event_type = ObservableActionType.ACTION_UPDATE

    def __init__(self):
        super().__init__()
        ObserverService.register_observer(self)

    @property
    def event_type(self):
        return self.__event_type

    def notify(self, obj, *args) -> bool:
        try:
            new_object = list(args)[0]
            if not obj or obj.name != new_object.name:
                return False
            PostProcessor.update(obj, new_object)
            return True
        except:
            return False


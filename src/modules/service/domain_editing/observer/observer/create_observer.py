import re

from src.modules.domain.enum.filter_types import FilterType
from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.service.domain_editing.observer.observer.abstract_observer import AbstractObserverHandler
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService
from src.modules.service.domain_editing.post_processing.post_processor import PostProcessor


class CreateObserverHandler(AbstractObserverHandler):
    __event_type = ObservableActionType.ACTION_CREATE

    def __init__(self):
        super().__init__()
        ObserverService.register_observer(self)

    def notify(self, obj, *args) -> bool:
        class_name = obj.__class__.__name__
        formatted_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
        proto = DomainPrototype().create_from_repository(formatted_name)
        if proto.filter_by(field_name="name", filter_type=FilterType.EQUALS, value=obj.name).first() is None:
            PostProcessor.create(obj)
            return True
        return False

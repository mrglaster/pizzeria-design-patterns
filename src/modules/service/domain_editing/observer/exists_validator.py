import re

from src.modules.domain.enum.filter_types import FilterType
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.service.domain_editing.observer.observer import Observer


class ExistsValidator(Observer):
    def notify(self, obj, *kwargs) -> bool:
        class_name = obj.__class__.__name__
        formatted_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
        proto = DomainPrototype().create_from_repository(formatted_name)
        exists = proto.filter_by(field_name="name", filter_type=FilterType.EQUALS, value=obj.name).first() is not None
        return exists


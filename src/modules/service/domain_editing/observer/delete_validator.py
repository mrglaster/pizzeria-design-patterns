import re

from src.modules.domain.enum.filter_types import FilterType
from src.modules.factory.repository_factory.repository_factory import RepositoryFactory
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.service.domain_editing.observer.observer import Observer


class DeleteValidator(Observer):
    __repository_factory = RepositoryFactory()

    def notify(self, obj, *kwargs) -> bool:
        class_name = obj.__class__.__name__
        formatted_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
        repos = list(self.__repository_factory.repositories.keys())
        for repo in repos:
            if repo == formatted_name:
                continue
            proto = DomainPrototype().create_from_repository(repo)
            first = proto.filter_by(field_name=formatted_name, value=obj,
                                                   filter_type=FilterType.EQUALS).first()
            if first:
                return False
        return True

import re

from src.modules.convertion.converter.json_converter import JSONConverter
from src.modules.domain.enum.filter_types import FilterType
from src.modules.domain.enum.log_enums import LogLevel
from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.factory.repository_factory.repository_factory import RepositoryFactory
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.service.domain_editing.observer.observer.abstract_observer import AbstractObserverHandler
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService
from src.modules.service.domain_editing.post_processing.post_processor import PostProcessor
from src.modules.service.logging.logger.service.logger_service import LoggerService


class DeleteObserverHandler(AbstractObserverHandler):
    __repository_factory = RepositoryFactory()

    __event_type = ObservableActionType.ACTION_DELETE

    def __init__(self):
        super().__init__()
        ObserverService.register_observer(self)

    @property
    def event_type(self):
        return self.__event_type

    def notify(self, obj, *args) -> bool:
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
                LoggerService.send_log(LogLevel.WARNING, f"Unable to delete object {JSONConverter.serialize(first)}: object in use")
                return False
        PostProcessor.delete(obj)
        return True

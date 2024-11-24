from src.modules.convertion.converter.json_converter import JSONConverter
from src.modules.domain.enum.log_enums import LogLevel
from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.service.domain_editing.observer.observer.abstract_observer import AbstractObserverHandler
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService
from src.modules.service.domain_editing.post_processing.post_processor import PostProcessor
from src.modules.service.logging.logger.service.logger_service import LoggerService


class UpdateObserverHandler(AbstractObserverHandler):
    __event_type = ObservableActionType.ACTION_UPDATE

    def __init__(self):
        super().__init__()
        ObserverService.register_observer(self)

    @property
    def event_type(self):
        return self.__event_type

    def notify(self, obj, *args) -> bool:
        try:
            new_object = list(args)[0][0]
            if not obj or obj.uid != new_object.uid:
                LoggerService.send_log(LogLevel.ERROR, f"Unable to update object {JSONConverter.serialize(obj)} to {JSONConverter.serialize(new_object)}!")
                return False
            PostProcessor.update(obj, new_object)
            LoggerService.send_log(LogLevel.DEBUG, f"Object {JSONConverter.serialize(obj)} was successfully updated to {JSONConverter.serialize(new_object)}!")
            return True
        except Exception as e:
            LoggerService.send_log(LogLevel.ERROR, str(e))
            print(f"EXCEPTION HAPPENED!!!!!: {e}")
            return False


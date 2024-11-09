from src.modules.service.domain_editing.observer.observer import Observer


class UpdateObserver(Observer):

    def notify(self, obj, *kwargs) -> bool:
        if not obj or obj.name != kwargs[0].name:
            return False


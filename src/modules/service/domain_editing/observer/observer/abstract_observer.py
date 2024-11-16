from abc import ABC, abstractmethod

class AbstractObserverHandler(ABC):

    @abstractmethod
    def notify(self, obj, *args) -> bool:
        pass
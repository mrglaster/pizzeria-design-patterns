from abc import ABC, abstractmethod

class AbstractObserver(ABC):

    @abstractmethod
    def notify(self, obj, *args) -> bool:
        pass
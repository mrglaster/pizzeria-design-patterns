import uuid
from abc import abstractmethod, ABC
from src.modules.validation.data_validator import DataValidator


class AbstractReference(ABC):
    __uid: str = ""
    _name: str = ""

    def __init__(self, name: str = 'DEFAULT_NAME', restrictions_property_name: str = "abstract_name", uid: str = ''):
        super().__init__()
        DataValidator.check_class_field(restrictions_property_name, str, name, True)
        self._name = name
        if uid:
            self.__uid = uid
        else:
            self.__uid = str(uuid.uuid4())

    @property
    def uid(self) -> str:
        return self.__uid

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        DataValidator.check_class_field("abstract_name", str, value)
        self._name = value

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        return not self == other

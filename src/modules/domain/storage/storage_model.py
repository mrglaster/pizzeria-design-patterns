from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.domain.storage.storage_address import Address


class Storage(AbstractReference):
    __address: Address = None

    @classmethod
    def create(cls, address: Address = None, name: str= "DEFAULT_STORAGE_NAME"):
        instance = cls()
        instance.__address = address
        instance.name = name
        return instance


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    def __eq__(self, other):
        if not isinstance(other, Storage):
            return False
        return self.__address == other.address

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.__address)

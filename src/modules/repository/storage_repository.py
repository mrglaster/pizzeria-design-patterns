from src.modules.domain.storage.storage_address import Address
from src.modules.domain.storage.storage_model import Storage
from src.modules.repository.data_repository import AbstractRepository
from src.modules.repository.storage_address_repository import StorageAddressRepository
from src.modules.service.data_loader.storage_data_loader import StorageDataLoader
from src.modules.validation.data_validator import DataValidator


class StorageRepository(AbstractRepository):
    __storages = {}

    @staticmethod
    def find_by_name(name: str):
        if name in StorageRepository.__storages:
            return StorageRepository.__storages[name]
        return None

    @staticmethod
    def clear():
        StorageRepository.__storages = {}

    @staticmethod
    def get_all():
        return StorageRepository.__storages

    @staticmethod
    def create_storage(name: str, address: Address) -> Storage:
        if name not in StorageRepository.__storages:
            storage = Storage()
            storage.create(address=address, name=name)
            StorageRepository.__storages[name] = storage
            return storage
        return StorageRepository.__storages[name]

    @staticmethod
    def add_storage(storage: Storage):
        DataValidator.validate_field_type(storage, Storage)
        if storage.name not in StorageRepository.__storages:
            StorageRepository.__storages[storage.name] = storage

    @staticmethod
    def load_from_json_file(file_path):
        storages = StorageDataLoader.load_from_json_file(file_path)
        for i in storages:
            StorageRepository.add_storage(i)
            StorageAddressRepository.add_address(i.address)
            
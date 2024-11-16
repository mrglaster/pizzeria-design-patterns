from src.modules.domain.storage.storage_address import Address
from src.modules.repository.data_repository import AbstractRepository
from src.modules.service.data_loader.storage_addresses_data_loader import StorageAddressesDataLoader
from src.modules.validation.data_validator import DataValidator


class StorageAddressRepository(AbstractRepository):
    __addresses = {}

    @staticmethod
    def create_address(country: str, region: str, city: str, street: str, building_number: str) -> Address:
        key = f"{country}_{region}_{city}_{street}_{building_number}"
        if key not in StorageAddressRepository.__addresses:
            address = Address()
            address.create(country, region, city, street, building_number)
            StorageAddressRepository.__addresses[key] = address
            return address
        return StorageAddressRepository.__addresses[key]

    @staticmethod
    def add(addr: Address):
        DataValidator.validate_field_type(addr, Address)
        key = f"{addr.country}_{addr.region}_{addr.city}_{addr.street}_{addr.building_number}"
        StorageAddressRepository.__addresses[key] = addr

    @staticmethod
    def find_by_name(name: str):
        if name in StorageAddressRepository.__addresses:
            return StorageAddressRepository.__addresses[name]
        return None

    @staticmethod
    def find_by_address(country: str, region: str, city: str, street: str, building_number: str) -> Address:
        key = f"{country}_{region}_{city}_{street}_{building_number}"
        DataValidator.validate_field_type(country, str, False)
        DataValidator.validate_field_type(region, str, False)
        DataValidator.validate_field_type(city, str, False)
        DataValidator.validate_field_type(street, str, False)
        DataValidator.validate_field_type(building_number, str, False)
        return StorageAddressRepository.__addresses.get(key)

    @staticmethod
    def load_addresses_from_json(json_file: str):
        addresses = StorageAddressesDataLoader.load_from_json_file(json_file)
        for address_data in addresses:
            StorageAddressRepository.add(address_data)

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(StorageAddressRepository, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_all():
        return StorageAddressRepository.__addresses

    @staticmethod
    def clear():
        StorageAddressRepository.__addresses = {}

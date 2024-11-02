import json

from src.modules.convertion.converter.json_converter import JSONConverter
from src.modules.service.data_loader.abstract_loader import AbstractDataLoader


class StorageAddressesDataLoader(AbstractDataLoader):
    @staticmethod
    def load_from_json_file(json_file: str):
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            result = []
            for i in json_data["addresses"]:
                new_address = JSONConverter.deserialize("storage_address", i)
                result.append(i)
        return result
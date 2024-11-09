import json

from src.modules.convertion.converter.json_converter import JSONConverter
from src.modules.service.data_loader.abstract_loader import AbstractDataLoader


class StorageDataLoader(AbstractDataLoader):

    @staticmethod
    def load_from_json_file(json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            result = []
            for storage in json_data["storages"]:
                new_storage = JSONConverter.deserialize("storage", storage)
                result.append(new_storage)
            return result
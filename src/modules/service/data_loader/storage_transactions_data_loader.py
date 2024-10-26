import json

from src.modules.convertion.converter.json_converter import JSONConverter
from src.modules.service.data_loader.abstract_loader import AbstractDataLoader


class StorageTransactionsDataLoader(AbstractDataLoader):

    @staticmethod
    def load_from_json_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            result = []
            for i in json_data["StorageTransaction"]:
                res = JSONConverter.deserialize("storage_transaction", i)
                result.append(res)
            return result
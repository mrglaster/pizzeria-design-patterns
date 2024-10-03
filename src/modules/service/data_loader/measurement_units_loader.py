from src.modules.service.data_loader.abstract_loader import AbstractDataLoader
import json


class MeasurementUnitsLoader(AbstractDataLoader):

    @staticmethod
    def load_from_json_file(file_path):
        try:
            with open(file_path, 'r') as f:
                json_data = json.load(f)["units"]
                return json_data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading JSON file: {e}")
            return None

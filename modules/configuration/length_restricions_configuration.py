import json
import os
from modules.exception.conf_file_not_found import ConfigurationFileNotFound


class LengthRestrictionsLoader:

    @staticmethod
    def get_restrictions(json_restrictions_path='configuration/length_restrictions.json'):
        processed_path = os.path.join(os.getcwd(), json_restrictions_path)
        processed_path = processed_path.replace("test/", "")
        if not os.path.exists(processed_path):
            raise ConfigurationFileNotFound(f"Configuration file {processed_path} not found!")
        with open(processed_path) as json_data:
            return json.load(json_data)

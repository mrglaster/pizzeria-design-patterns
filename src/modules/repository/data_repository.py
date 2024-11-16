import datetime
import json
import os.path
import re

from src.modules.convertion.converter.json_converter import JSONConverter
from src.modules.domain.report.report.plain_text.report_json import ReportJSON
from src.modules.service.base.abstract_logic import AbstractLogic
from src.modules.service.managers.settings_manager import SettingsManager


class AbstractRepository(AbstractLogic):

    def set_exception(self, ex: Exception):
        pass

    @staticmethod
    def find_by_name(name: str):
        pass

    @staticmethod
    def clear():
       pass

    @staticmethod
    def get_all() -> dict:
        pass

    @staticmethod
    def add(obj):
        pass

    @staticmethod
    def delete(obj):
        pass

    @staticmethod
    def update(old_object, new_object):
        pass

    @classmethod
    def dump(cls):
        try:
            from src.modules.domain.report.report_format.report_format import ReportFormat
            data = list(cls.get_all().values())
            report = ReportJSON()
            report.create(data)
            output_data = report.get_result()
            class_name = cls.__name__
            formatted_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower().replace("_repository", "")
            file_name = f"{datetime.datetime.utcnow()}.json"
            output_dir = os.path.join(SettingsManager().settings.dumps_path, formatted_name)
            os.makedirs(output_dir, exist_ok=True)
            file_name = file_name.replace(' ', '_')
            output_path = os.path.join(output_dir, file_name)
            with open(output_path, 'w') as file:
                file.write(output_data)
            return True
        except:
            return False

    @classmethod
    def load_dump(cls, clear_repository: bool = True):
        class_name = cls.__name__
        formatted_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower().replace("_repository", "")
        dir_path = os.path.join(SettingsManager().settings.dumps_path, formatted_name)
        files = [f for f in os.listdir(dir_path) if f.endswith('.json')]
        latest_file = max(files, key=lambda f: datetime.datetime.strptime(f.split('.')[0], '%Y-%m-%d_%H:%M:%S'))
        latest_file_path = os.path.join(dir_path, latest_file)
        if clear_repository:
            cls.clear()
        with open(latest_file_path, 'r') as file:
            data = json.load(file)
            key_name = list(data.keys())[0]
            for obj in data[key_name]:
                obj_instance = JSONConverter.deserialize(formatted_name, obj)
                cls.add(obj_instance)
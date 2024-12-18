import json
import os
from datetime import datetime

from src.modules.domain.settings.settings_model import Settings


class SettingsManager:
    """
    The `SettingsManager` class manages the reading, writing, and validation of settings
    stored in a JSON file. It also provides methods to retrieve and update settings values.

    Attributes:
        __file_name (str): The name of the settings file.
        __settings (Settings): An instance of the `Settings` class.
        __logger (Logger): Logger instance for logging messages and errors.
    """

    __file_name = "settings.json"
    __settings: Settings = Settings()

    def __new__(cls):
        """
        Implements the Singleton pattern, ensuring that only one instance of `SettingsManager` exists.

        Returns:
            SettingsManager: The single instance of the SettingsManager class.
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(SettingsManager, cls).__new__(cls)
        return cls.instance

    def read_settings(self, file_name: str = ""):
        """
        Reads the settings from a JSON file and updates the `Settings` instance with the loaded values.

        Args:
            file_name (str): Optional custom file name for the settings file.

        Returns:
            bool: True if all fields are successfully loaded, False otherwise.

        Raises:
            TypeError: If the provided file name is not a string.
        """
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument")
        if file_name != "":
            self.__file_name = file_name
        try:
            full_name = os.path.join(os.getcwd(), 'configuration', self.__file_name).replace('test/', '').replace(
                'tests/', '').replace('src/', '')
            fields_counter = 0
            with open(full_name) as json_data:
                data = json.load(json_data)
                fields = dir(self.__settings)
                for field in fields:
                    if field in data.keys():
                        self.__settings.__setattr__(field, data[field])
                        fields_counter += 1
                if os.path.sep not in self.__settings.reports_path:
                    project_path = os.getcwd()
                    project_path = project_path.replace('tests/', '').replace('test/', '')
                    reports_path = self.__settings.reports_path
                    reports_path = os.path.join(project_path, reports_path).replace('tests/', '').replace('test/',
                                                                                                          '').replace(
                        'tests/', '').replace('test/', '').replace('src/', '')
                    self.__settings.reports_path = os.path.join(project_path, reports_path)

                if not os.path.exists(self.__settings.reports_path):
                    return False

                if os.path.sep not in self.__settings.dumps_path:
                    project_path = os.getcwd()
                    project_path = project_path.replace('tests/', '').replace('test/', '')
                    dumps_path = self.__settings.dumps_path
                    dumps_path = os.path.join(project_path, dumps_path).replace('tests/', '').replace('test/',
                                                                                                      '').replace(
                        'tests/', '').replace('test/', '').replace('src/', '')
                    self.__settings.dumps_path = os.path.join(project_path, dumps_path)
                if os.path.sep not in self.__settings.logs_path:
                    project_path = os.getcwd()
                    project_path = project_path.replace('tests/', '').replace('test/', '')
                    logs_path = self.__settings.logs_path
                    logs_path = os.path.join(project_path, logs_path).replace('tests/', '').replace('test/',
                                                                                                    '').replace(
                        'tests/', '').replace('test/', '').replace('src/', '')
                    self.__settings.logs_path = os.path.join(logs_path, logs_path)

                if os.path.sep not in self.__settings.migrations_path:
                    project_path = os.getcwd()
                    project_path = project_path.replace('tests/', '').replace('test/', '')
                    migrations_path = self.__settings.migrations_path
                    migrations_path = os.path.join(project_path, migrations_path).replace('tests/', '').replace('test/',
                                                                                                    '').replace(
                        'tests/', '').replace('test/', '').replace('src/', '')
                    self.__settings.migrations_path = migrations_path

                if fields_counter != self.__settings.get_prop_count() - 2:
                    return False
                return True
        except Exception as e:
            self.__settings = self.__default_settings()
            return False
        finally:
            return self.__settings

    @property
    def settings(self):
        """Gets the current settings instance."""
        return self.__settings

    def update_first_run(self):
        self.settings.first_run = False
        full_name = os.path.join(os.getcwd(), 'configuration', "settings.json").replace('test/', '').replace('tests/',
                                                                                                              '').replace(
            'src/', '')
        if not os.path.exists(full_name):
            return False
        with open(full_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if "first_run" in data:
            data["first_run"] = False
            with open(full_name, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return True
        return False

    @staticmethod
    def __default_settings():
        """
        Provides default settings values in case the settings file is missing or corrupted.

        Returns:
            Settings: A `Settings` object populated with default values.
        """
        data = Settings()
        data.inn = "0" * 12
        data.organization_name = "DEFAULT_ORG_NAME"
        data.director_name = "DEFAULT_DIRECTOR_NAME"
        data.bank_account = "0" * 11
        data.correspondent_account = "0" * 11
        data.property_type = "0" * 5
        data.bik = "0" * 9
        data.recipes_path = f"{os.getcwd().replace('/tests', '').replace('/test', '').replace('src/', '')}/docs"
        data.reports_path = f"{os.getcwd().replace('/tests', '').replace('/test', '').replace('src/', '')}/reports"
        data.dumps_path = f"{os.getcwd().replace('/tests', '').replace('/test', '').replace('src/', '')}/dumps"
        data.logs_path = f"{os.getcwd().replace('/tests', '').replace('/test', '').replace('src/', '')}/logs"
        data.migrations_path = f"{os.getcwd().replace('/tests', '').replace('/test', '').replace('src/', '')}/migrations"
        data.use_db = False
        data.default_convertion_format = "FORMAT_CSV"
        data.blocking_date = datetime.strptime("2007-09-01", "%Y-%m-%d %Y-%m-%d %H:%M:%S.%f")
        data.first_run = True
        return data

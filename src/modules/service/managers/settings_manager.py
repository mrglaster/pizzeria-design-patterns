import json
import os
import logging
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
    __logger = logging.getLogger(__name__)

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
            full_name = os.path.join(os.curdir, self.__file_name)
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
                    reports_path = self.__settings.reports_path.replace('tests/', '').replace('test/', '').replace('tests/', '').replace('test/', '')
                    self.__settings.reports_path = os.path.join(project_path, reports_path)

                if not os.path.exists(self.__settings.reports_path):
                    self.__logger.error("Provided reports path does not exist!")
                    return False
                if fields_counter != self.__settings.get_prop_count():
                    self.__logger.error("Not all the expected settings fields have been loaded!")
                    return False
                return True
        except Exception as e:
            self.__logger.error(f"Exception happened: {e}")
            self.__logger.warning("Using default values for missing settings fields")
            self.__settings = self.__default_settings()
            return False
        finally:
            return self.__settings

    @property
    def settings(self):
        """Gets the current settings instance."""
        return self.__settings

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
        data.recipes_path = f"{os.getcwd().replace('/tests', '').replace('/test', '')}/docs"
        data.reports_path = f"{os.getcwd().replace('/tests', '').replace('/test', '')}/reports"
        data.default_convertion_format = "FORMAT_CSV"
        return data

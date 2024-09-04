import json
import os


class Settings:
    __organization_name = ""
    __inn = ""
    __director_name = ""

    @property
    def organization_name(self):
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError(f"Invalid argument type {type(value)}! String expected")
        self.__organization_name = value

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Invalid argument type {type(value)}! String expected")
        self.__inn = value

    @property
    def director_name(self):
        return self.__director_name

    @director_name.setter
    def director_name(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Invalid argument type {type(value)}! String expected")
        self.__director_name = value

    def __str__(self):
        return f"Settings ({self.organization_name} -  {self.director_name} -  {self.inn})"


def __default_settings():
    data = Settings()
    data.inn = "DEFAULT_INN"
    data.organization_name = "DEFAULT_ORG_NAME"
    data.director_name = "DEFAULT_DIRECTOR_NAME"
    return data


class SettingsManager:
    __file_name = "settings.json"
    __settings: Settings = Settings()

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SettingsManager, cls).__new__(cls)
        return cls.instance

    def read_settings(self, file_name: str = ""):
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument")
        if file_name != "":
            self.__file_name = file_name
        try:
            full_name = os.path.join(os.curdir, self.__file_name)
            with open(full_name) as json_data:
                data = json.load(json_data)
                fields = dir(self.__settings)
                for field in fields:
                    if field in data.keys():
                        self.__settings.__setattr__(field, data[field])
        finally:
            return self.__settings

    @property
    def settings(self):
        return self.__settings

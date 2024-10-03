from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.domain.settings.settings_model import Settings
from src.modules.validation.data_validator import DataValidator


class Organization(AbstractReference):
    __inn = ""
    __bank_account = ""
    __bik = ""
    __property_type = ""

    def __init__(self, settings: Settings):
        super().__init__(settings.organization_name, "organization_name")
        self.__inn = settings.inn
        self.__bank_account = settings.bank_account
        self.__bik = settings.bik
        self.__property_type = settings.property_type

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        DataValidator.check_class_field("inn", str, value)
        self.__inn = value

    @property
    def bank_account(self):
        return self.__bank_account

    @bank_account.setter
    def bank_account(self, value: str):
        DataValidator.check_class_field("bank_account", str, value)
        self.__bank_account = value

    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value: str):
        DataValidator.check_class_field("bik", str, value)
        self.__bik = value

    @property
    def property_type(self):
        return self.__property_type

    @property_type.setter
    def property_type(self, value: str):
        DataValidator.check_class_field("property_type", str, value)
        self.__property_type = value

    def __eq__(self, other):
        if not isinstance(other, Organization):
            return False
        return self._name == other._name

    def __ne__(self, other):
        return not self == other
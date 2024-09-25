from __future__ import annotations
from modules.domain.base.abstract_reference import AbstractReference
from modules.validation.data_validator import DataValidator


class Settings(AbstractReference):
    """
    The `Settings` class encapsulates the configuration details such as organization name,
    INN (taxpayer identification number), director name, bank bank_account details, and property type.
    It provides getter and setter methods for each field, ensuring that the data is validated
    according to specified rules before being stored.

    Attributes:
        __organization_name (str): Name of the organization.
        __inn (str): Taxpayer Identification Number (INN).
        __director_name (str): Name of the director.
        __bank_account (str): Bank bank_account number.
        __correspondent_account (str): Correspondent bank_account number.
        __bik (str): Bank Identifier Code (BIK).
        __property_type (str): Type of property.
        __validator (DataValidator): Validator instance for validating field data.
    """

    __organization_name = ""
    __inn = ""
    __director_name = ""
    __bank_account = ""
    __correspondent_account = ""
    __bik = ""
    __property_type = ""
    __recipes_path = ""
    __reports_path = ""
    __default_convertion_format = ""

    @property
    def organization_name(self):
        """Gets the name of the organization."""
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        """Sets and validates the name of the organization."""
        DataValidator.check_class_field("organization_name", str, value)
        self.__organization_name = value

    @property
    def inn(self):
        """Gets the INN (Taxpayer Identification Number)."""
        return self.__inn

    @inn.setter
    def inn(self, value):
        """Sets and validates the INN."""
        DataValidator.check_class_field("inn", str, value)
        self.__inn = value

    @property
    def director_name(self):
        """Gets the name of the director."""
        return self.__director_name

    @director_name.setter
    def director_name(self, value):
        """Sets and validates the name of the director."""
        DataValidator.check_class_field("director_name", str, value)
        self.__director_name = value

    @property
    def bank_account(self):
        """Gets the bank bank_account number."""
        return self.__bank_account

    @bank_account.setter
    def bank_account(self, value):
        """Sets and validates the bank bank_account number."""
        DataValidator.check_class_field("bank_account", str, value)
        self.__bank_account = value

    @property
    def correspondent_account(self):
        """Gets the correspondent bank_account number."""
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value):
        """Sets and validates the correspondent bank_account number."""
        DataValidator.check_class_field("correspondent_account", str, value)
        self.__correspondent_account = value

    @property
    def bik(self):
        """Gets the BIK (Bank Identifier Code)."""
        return self.__bik

    @bik.setter
    def bik(self, value):
        """Sets and validates the BIK."""
        DataValidator.check_class_field("bik", str, value)
        self.__bik = value

    @property
    def property_type(self):
        """Gets the property type."""
        return self.__property_type

    @property_type.setter
    def property_type(self, value):
        """Sets and validates the property type."""
        DataValidator.check_class_field("property_type", str, value)
        self.__property_type = value

    def get_prop_count(self):
        """
        Returns the number of properties (fields) in the Settings class.

        Returns:
            int: The number of properties.
        """
        return len(self.__dict__.keys())

    @property
    def recipes_path(self):
        return self.__recipes_path

    @recipes_path.setter
    def recipes_path(self, value):
        DataValidator.validate_field_type(value, str)
        self.__recipes_path = value

    @property
    def reports_path(self):
        return self.__reports_path

    @reports_path.setter
    def reports_path(self, value):
        DataValidator.validate_field_type(value, str)
        self.__reports_path = value

    @property
    def default_convertion_format(self):
        return self.__default_convertion_format

    @default_convertion_format.setter
    def default_convertion_format(self, value: str):
        DataValidator.validate_field_type(value, str)
        DataValidator.validate_report_export_type(value)
        self.__default_convertion_format = value

    def __str__(self):
        """
        Returns a string representation of the Settings object.

        Returns:
            str: String representation of the Settings.
        """
        result = "Settings("
        class_dict = self.__dict__
        for key in class_dict.keys():
            result += f"{key.replace('_Settings__', '')} : {class_dict[key]} "
        result += ")"
        return result

    def __eq__(self, other):
        try:
            assert isinstance(other, Settings)
            assert self.__organization_name == other.__organization_name
            assert self.__inn == other.__inn
            assert self.__director_name == other.__director_name
            assert self.__bank_account == other.__bank_account
            assert self.__correspondent_account == other.__correspondent_account
            assert self.__bik == other.__bik
            assert self.__property_type == other.__property_type
            assert self.__reports_path == other.__reports_path
            return True
        except:
            return False

    def __ne__(self, other):
        return self != other

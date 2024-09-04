from modules.settings.settings_validator import SettingsValidator


class Settings:
    """
    The `Settings` class encapsulates the configuration details such as organization name,
    INN (taxpayer identification number), director name, bank account details, and property type.
    It provides getter and setter methods for each field, ensuring that the data is validated
    according to specified rules before being stored.

    Attributes:
        __organization_name (str): Name of the organization.
        __inn (str): Taxpayer Identification Number (INN).
        __director_name (str): Name of the director.
        __bank_account (str): Bank account number.
        __correspondent_account (str): Correspondent account number.
        __bik (str): Bank Identifier Code (BIK).
        __property_type (str): Type of property.
        __validator (SettingsValidator): Validator instance for validating field data.
    """

    __organization_name = ""
    __inn = ""
    __director_name = ""
    __bank_account = ""
    __correspondent_account = ""
    __bik = ""
    __property_type = ""
    __validator = SettingsValidator()

    @property
    def organization_name(self):
        """Gets the name of the organization."""
        return self.__organization_name

    @organization_name.setter
    def organization_name(self, value: str):
        """Sets and validates the name of the organization."""
        self.__validator.validate_field("organization_name", str, value)
        self.__organization_name = value

    @property
    def inn(self):
        """Gets the INN (Taxpayer Identification Number)."""
        return self.__inn

    @inn.setter
    def inn(self, value):
        """Sets and validates the INN."""
        self.__validator.validate_field("inn", str, value)
        self.__inn = value

    @property
    def director_name(self):
        """Gets the name of the director."""
        return self.__director_name

    @director_name.setter
    def director_name(self, value):
        """Sets and validates the name of the director."""
        self.__validator.validate_field(value, str, value)
        self.__director_name = value

    @property
    def bank_account(self):
        """Gets the bank account number."""
        return self.__bank_account

    @bank_account.setter
    def bank_account(self, value):
        """Sets and validates the bank account number."""
        self.__validator.validate_field("bank_account", str, value)
        self.__bank_account = value

    @property
    def correspondent_account(self):
        """Gets the correspondent account number."""
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value):
        """Sets and validates the correspondent account number."""
        self.__validator.validate_field("correspondent_account", str, value)
        self.__correspondent_account = value

    @property
    def bik(self):
        """Gets the BIK (Bank Identifier Code)."""
        return self.__bik

    @bik.setter
    def bik(self, value):
        """Sets and validates the BIK."""
        self.__validator.validate_field("bik", str, value)
        self.__bik = value

    @property
    def property_type(self):
        """Gets the property type."""
        return self.__property_type

    @property_type.setter
    def property_type(self, value):
        """Sets and validates the property type."""
        self.__validator.validate_field("property_type", str, value)
        self.__property_type = value

    def get_prop_count(self):
        """
        Returns the number of properties (fields) in the Settings class.

        Returns:
            int: The number of properties.
        """
        return len(self.__dict__.keys())

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

class SettingsValidator:
    """
    The `SettingsValidator` class is responsible for validating the fields of the `Settings` class.
    It ensures that the types and lengths of the fields are correct based on predefined restrictions.

    Attributes:
        __length_restrictions (dict): Dictionary containing the length restrictions for each field.
    """

    __length_restrictions = {
        "inn": 12,
        "bank_account": 11,
        "correspondent_account": 11,
        "bik": 9,
        "property_type": 5,
        "organization_name": None,
        "director_name": None
    }

    def __new__(cls):
        """
        Implements the Singleton pattern, ensuring that only one instance of `SettingsValidator` exists.

        Returns:
            SettingsValidator: The single instance of the SettingsValidator class.
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(SettingsValidator, cls).__new__(cls)
        return cls.instance

    def __validate_field_type(self, value, expected_type):
        """
        Validates that the type of the given value matches the expected type.

        Args:
            value: The value to validate.
            expected_type: The expected type of the value.

        Raises:
            TypeError: If the value is not of the expected type.
        """
        if not isinstance(value, expected_type):
            raise TypeError(f"Invalid argument type {type(value)}! {expected_type.__name__} expected")

    def __validate_length(self, value, field_name):
        """
        Validates that the length of the given value matches the expected length for the field.

        Args:
            value (str): The value to validate.
            field_name (str): The name of the field being validated.

        Raises:
            ValueError: If the length of the value does not match the expected length.
        """
        expected_length = self.__length_restrictions.get(field_name)
        if expected_length is not None and len(value) != expected_length or expected_length is None and len(value) == 0:
            raise ValueError(f"{field_name.capitalize()} length must be {expected_length} characters")

    def validate_field(self, field_name, expected_type, value):
        """
        Validates a field's value against its expected type and length.

        Args:
            field_name (str): The name of the field being validated.
            expected_type: The expected type of the field.
            value: The value of the field to validate.

        Raises:
            TypeError: If the value is not of the expected type.
            ValueError: If the length of the value is incorrect.
        """
        self.__validate_field_type(value=value, expected_type=expected_type)
        self.__validate_length(value=value, field_name=field_name)


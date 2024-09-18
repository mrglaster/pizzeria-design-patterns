from modules.configuration.length_restricions_configuration import LengthRestrictionsLoader
from modules.exception.bad_argument_exception import BadArgumentException


class DataValidator:
    __length_restrictions_loader = LengthRestrictionsLoader()

    @staticmethod
    def validate_field_type(value, expected_type, nullable=False):
        if not isinstance(value, expected_type) and not nullable:
            raise BadArgumentException(f"Invalid argument type {type(value)}! {expected_type.__name__} expected")

    @staticmethod
    def validate_length_restriction(value, expected_length: int = 0):
        if expected_length == -1:
            return
        if value is not None:
            value_len = len(str(value))
            if expected_length > 0 and 0 < value_len <= expected_length:
                return
            raise BadArgumentException(
                f"The length of provided value does not correspond the length restriction: {expected_length}")
        raise BadArgumentException("None provided! Value expected!")

    @staticmethod
    def validate_exact_field_length(value, expected_length: int = 0):
        if value is not None:
            value_len = len(str(value))

            if 0 < expected_length == value_len:
                return
            raise BadArgumentException(
                f"The length of provided value does not correspond the length restriction: {expected_length}")
        raise BadArgumentException("None provided! Value expected!")

    @staticmethod
    def check_class_field(property_name, property_class, property_value, nullable=False):
        DataValidator.validate_field_type(property_value, property_class)
        restrictions = LengthRestrictionsLoader.get_restrictions()
        DataValidator.validate_length_restriction(property_value, restrictions[property_name])
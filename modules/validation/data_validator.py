from modules.configuration.length_restricions_configuration import LengthRestrictionsLoader
from modules.domain.report.report_format.report_format import ReportFormat
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
        if property_name in restrictions.keys():
            DataValidator.validate_length_restriction(property_value, restrictions[property_name])

    @staticmethod
    def validate_list_not_empty(value: list):
        if not len(value):
            raise BadArgumentException("The list you provided is empty!")

    @staticmethod
    def validate_str_not_empty(value: str):
        if not len(value):
            raise BadArgumentException("Empty string provided!")

    @staticmethod
    def validate_report_export_type(value: str):
        try:
            test = ReportFormat[value]
        except:
            raise BadArgumentException(f"Report export format not implemented: {value}")
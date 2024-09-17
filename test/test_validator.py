import unittest

from modules.exception.bad_argument_exception import BadArgumentException
from modules.service.util.validation.data_validator import DataValidator


class TestUtils(unittest.TestCase):
    def test_check_field_types_valid(self):
        DataValidator.validate_field_type("123", str)
        DataValidator.validate_field_type(228, int)
        DataValidator.validate_field_type({}, dict)

    def test_check_invalid_field_type(self):
        with self.assertRaises(BadArgumentException):
            DataValidator.validate_field_type("123", dict)

    def test_check_maxlen_restriction_valid(self):
        DataValidator.validate_length_restriction("123", 10)

    def test_check_maxlen_restriction_invalid(self):
        with self.assertRaises(BadArgumentException):
            DataValidator.validate_length_restriction("123", 1)

    def test_check_exact_length_valid(self):
        DataValidator.validate_exact_field_length("123", 3)

    def test_check_exact_length_invalid(self):
        with self.assertRaises(BadArgumentException):
            DataValidator.validate_exact_field_length("123", 1)

    def test_no_length_restriction(self):
        DataValidator.validate_length_restriction("123", -1)

    def test_check_main_field_restrictions(self):
        DataValidator.check_class_field("inn", str, "123456789009")

    def test_check_main_field_restrictions_invalid(self):
        with self.assertRaises(BadArgumentException):
            DataValidator.check_class_field("inn", str,"")
import unittest

from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.provider.format.format_provider import FormatProvider


class TestApiUtils(unittest.TestCase):
    def test_valid_format_getting(self):
        report_formats = list(ReportFormat.__members__.keys())[:-1]
        for i in range(len(report_formats)):
            assert FormatProvider.get_format(report_formats[i]) == FormatProvider.get_format(str(i))

    def test_invalid_format_ordinal(self):
        with self.assertRaises(BadArgumentException):
            a = FormatProvider.get_format(str(228))

    def test_invalid_format_str(self):
        with self.assertRaises(BadArgumentException):
            a = FormatProvider.get_format("AZAZA")

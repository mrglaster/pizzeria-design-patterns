import unittest

from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.provider.format.format_provider import FormatProvider


class TestApi(unittest.TestCase):
    def test_valid_format_getting(self):
        report_formats = list(ReportFormat.__members__.keys())[:-1]
        for i in range(len(report_formats)):
            assert FormatProvider.get_format(report_formats[i]) == FormatProvider.get_format(str(i))

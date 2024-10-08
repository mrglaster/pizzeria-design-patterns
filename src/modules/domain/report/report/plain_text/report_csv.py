from src.modules.domain.report.report.base.abstract_report import PlainTextReport
from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.validation.data_validator import DataValidator


class ReportCSV(PlainTextReport):

    def __init__(self, settings_path=""):
        super().__init__(settings_path=settings_path)
        self.format = ReportFormat.FORMAT_CSV

    def create(self, data: list):
        DataValidator.validate_field_type(data, list)
        if not len(data):
            raise BadArgumentException("Empty data set provided!")
        used_model = data[0]
        fields = self.get_class_fields(used_model)
        for field in fields:
            self._result += f"{field};"
        self._result += '\n'
        for row in data:
            for field in fields:
                value = getattr(row, field)
                self._result += f"{value};"
            self._result += f"\n"


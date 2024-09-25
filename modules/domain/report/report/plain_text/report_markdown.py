from modules.domain.report.report.base.abstract_report import PlainTextReport
from modules.domain.report.report_format.report_format import ReportFormat
from modules.exception.bad_argument_exception import BadArgumentException
from modules.validation.data_validator import DataValidator


class ReportMD(PlainTextReport):

    def __init__(self, settings_path=""):
        super().__init__(settings_path=settings_path)
        self.format = ReportFormat.FORMAT_MARKDOWN

    def create(self, data: list):
        DataValidator.validate_field_type(data, list)
        if len(data) == 0:
            raise BadArgumentException("Empty data list provided")
        first_model = data[0]
        fields = self.get_class_fields(first_model)
        self._result = "|"
        divider = "|"
        for field in fields:
            self._result += f"{field}|"
            divider += "-" * (len(field)) + "|"
        self._result += "\n"
        self._result += divider + "\n"
        for row in data:
            self._result += "|"
            for field in fields:
                value = getattr(row, field)
                self._result += f"{value}|"
            self._result += "\n"

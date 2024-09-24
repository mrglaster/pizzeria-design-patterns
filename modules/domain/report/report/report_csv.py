from modules.domain.report.report.abstract_report import AbstractReport
from modules.domain.report.report_format.report_format import ReportFormat
from modules.exception.bad_argument_exception import BadArgumentException
from modules.validation.data_validator import DataValidator


class ReportCSV(AbstractReport):

    def __init__(self):
        super().__init__()
        self.__format = ReportFormat.FORMAT_CSV

    def create(self, output_file: str, data: list):
        DataValidator.validate_field_type(output_file, str)
        DataValidator.validate_field_type(data, list)
        if not len(data):
            raise BadArgumentException("Empty data set provided!")
        used_model = data[0]
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(used_model.__class__, x)), dir(used_model.__class__)))

        #writing header
        for field in fields:
            self._result += f"{field}"
        self._result += '\n'

        #writing data
        for row in data:
            for field in fields:
                value = getattr(row, field)
                self._result += f"{value};"
            self._result += f"\n"


    @property
    def format(self) -> ReportFormat:
        return ReportFormat.FORMAT_CSV

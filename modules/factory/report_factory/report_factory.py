from modules.domain.report.report.abstract_report import AbstractReport
from modules.domain.report.report.report_csv import ReportCSV
from modules.domain.report.report_format.report_format import ReportFormat
from modules.exception.bad_argument_exception import BadArgumentException
from modules.service.base.abstract_logic import AbstractLogic
from modules.validation.data_validator import DataValidator


class ReportFactory(AbstractLogic):
    __reports: dict = {

    }

    def set_exception(self, ex: Exception):
        pass

    def __init__(self):
        super().__init__()
        self.__reports[ReportFormat.FORMAT_CSV] = ReportCSV

    def get_report_class_instance(self, report_format: ReportFormat) -> AbstractReport:
        DataValidator.validate_field_type(report_format, ReportFormat)
        if report_format not in self.__reports:
            raise BadArgumentException(f"Unknown report format: {report_format}")
        report = self.__reports[report_format]
        return report()
from modules.domain.report.report.base.abstract_report import AbstractReport, PlainTextReport, ComplexReport
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
        subclasses = list(set(PlainTextReport.__subclasses__())) + list(set(ComplexReport.__subclasses__()))
        for report_class in subclasses:
            current_obj = report_class()
            self.__reports[current_obj.format] = report_class

    def get_report_class_instance(self, report_format: ReportFormat) -> AbstractReport:
        DataValidator.validate_field_type(report_format, ReportFormat)
        if report_format not in self.__reports or report_format == ReportFormat.FORMAT_ABSTRACT:
            raise BadArgumentException(f"Format not implemented: {report_format}")
        report = self.__reports[report_format]
        return report()
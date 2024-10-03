from src.modules.domain.report.report.base.abstract_report import AbstractReport, PlainTextReport, ComplexReport
from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.service.base.abstract_logic import AbstractLogic
from src.modules.service.managers.settings_manager import SettingsManager
from src.modules.validation.data_validator import DataValidator


class ReportFactory(AbstractLogic):
    __reports: dict = {}
    __settings_manager = None
    __default_export_type = None

    def set_exception(self, ex: Exception):
        pass

    def __init__(self, settings_path=""):
        super().__init__()
        subclasses = list(set(PlainTextReport.__subclasses__())) + list(set(ComplexReport.__subclasses__()))
        for report_class in subclasses:
            current_obj = report_class()
            self.__reports[current_obj.format] = report_class
        self.__settings_manager = SettingsManager()
        self.__settings_manager.read_settings(settings_path)
        self.__default_export_type = ReportFormat[self.__settings_manager.settings.default_convertion_format]

    def get_report_class_instance(self, report_format: ReportFormat) -> AbstractReport:
        DataValidator.validate_field_type(report_format, ReportFormat)
        if report_format not in self.__reports or report_format == ReportFormat.FORMAT_ABSTRACT:
            raise BadArgumentException(f"Format not implemented: {report_format}")
        report = self.__reports[report_format]
        return report()

    def create_default(self, data: list, output_file: str):
        report_generator = self.__reports[self.__default_export_type]()
        report_generator.crate(data)
        report_generator.save(output_file)

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ReportFactory, cls).__new__(cls)
        return cls.instance

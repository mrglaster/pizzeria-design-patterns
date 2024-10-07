from src.modules.domain.report.report.base.abstract_report import PlainTextReport
from src.modules.factory.report_factory.report_factory import ReportFactory
from src.modules.factory.repository_factory.repository_factory import RepositoryFactory
from src.modules.provider.format.format_provider import FormatProvider
from src.modules.validation.data_validator import DataValidator


class ReportDataProvider:
    repository_factory = RepositoryFactory()
    report_factory = ReportFactory()

    @staticmethod
    def get_requested_report(report_format: str, report_type: str) -> str:
        DataValidator.validate_field_type(report_type, str)
        DataValidator.validate_str_not_empty(report_type)
        report_format = FormatProvider.get_format(format_data=report_format)
        report = ReportDataProvider.report_factory.get_report_class_instance(report_format)
        data_repository = ReportDataProvider.repository_factory.get_by_name(report_type)()
        report.create(list(data_repository.get_all().values()))
        if issubclass(report.__class__, PlainTextReport):
            result = report.get_result()
            return result
        return report.get_result_b64()

    @staticmethod
    def is_valid_type(format_type: str):
        DataValidator.validate_field_type(format_type, str)
        DataValidator.validate_str_not_empty(format_type)
        return format_type in ReportDataProvider.repository_factory.repositories

    @staticmethod
    def is_valid_format(report_format: str):
        try:
            a = FormatProvider.get_format(format_data=report_format)
            return True
        except:
            return False

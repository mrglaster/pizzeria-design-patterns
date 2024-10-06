from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.validation.data_validator import DataValidator


class FormatProvider:

    @staticmethod
    def get_format(format_data: str):
        if format_data.isnumeric():
            return FormatProvider.get_format_by_ordinal(int(format_data))
        DataValidator.validate_report_export_type(format_data)
        return ReportFormat[format_data]

    @staticmethod
    def get_format_by_ordinal(ordinal):
        return ReportFormat.get_by_ordinal(ordinal)

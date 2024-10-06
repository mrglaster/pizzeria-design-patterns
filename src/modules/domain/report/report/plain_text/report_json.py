from src.modules.domain.report.report.base.abstract_report import PlainTextReport
from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.validation.data_validator import DataValidator


class ReportJSON(PlainTextReport):

    def __init__(self):
        super().__init__()
        self.format = ReportFormat.FORMAT_JSON

    def create(self, data: list):
        DataValidator.validate_field_type(data, list)
        if not len(data):
            raise BadArgumentException("Empty data list provided!")
        used_model = data[0]
        class_name = type(used_model).__name__
        result = {class_name: data}
        self._result = self._converter_factory.serialize(result, 'json')

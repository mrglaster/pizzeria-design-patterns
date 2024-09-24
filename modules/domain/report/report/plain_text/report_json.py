from modules.domain.report.report.base.abstract_report import PlainTextReport
from modules.domain.report.report_format.report_format import ReportFormat
from modules.exception.bad_argument_exception import BadArgumentException
from modules.validation.data_validator import DataValidator


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
        result = {class_name: []}
        fields = self.get_class_fields(used_model)
        for row in data:
            current_json = {}
            for field in fields:
                value = getattr(row, field)
                current_json[field] = str(value)
            result[class_name].append(current_json)
        self._result = str(result)

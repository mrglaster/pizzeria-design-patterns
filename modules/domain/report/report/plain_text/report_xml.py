import xml.etree.ElementTree as ET
from modules.domain.report.report.base.abstract_report import PlainTextReport
from modules.domain.report.report_format.report_format import ReportFormat
from modules.exception.bad_argument_exception import BadArgumentException
from modules.validation.data_validator import DataValidator


class ReportXML(PlainTextReport):

    def __init__(self):
        super().__init__()
        self.format = ReportFormat.FORMAT_XML

    def create(self, data: list):
        DataValidator.validate_field_type(data, list)
        if not len(data):
            raise BadArgumentException("Empty data list provided!")
        used_model = data[0]
        class_name = type(used_model).__name__
        root = ET.Element(class_name + 's')
        fields = list(filter(lambda x: not x.startswith("_") and not callable(getattr(used_model.__class__, x)),
                             dir(used_model.__class__)))
        for row in data:
            item = ET.SubElement(root, class_name)
            for field in fields:
                value = getattr(row, field)
                field_element = ET.SubElement(item, field)
                field_element.text = str(value)
        self._result = ET.tostring(root, encoding='unicode', method='xml')

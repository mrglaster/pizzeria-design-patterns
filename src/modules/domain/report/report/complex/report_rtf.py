import base64
import io
import os

from PyRTF.Elements import Document
from PyRTF.Renderer import Renderer
from PyRTF.document.paragraph import Paragraph, Table, Cell
from PyRTF.document.section import Section
from src.modules.domain.report.report.base.abstract_report import ComplexReport
from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.validation.data_validator import DataValidator


class ReportRTF(ComplexReport):
    def __init__(self, settings_file=""):
        super().__init__(settings_file)
        self.format = ReportFormat.FORMAT_RTF

    def create(self, data: list):
        def to_rtf_unicode(text):
            return ''.join([f'\\u{ord(char)}?' if ord(char) > 127 else char for char in text])

        DataValidator.validate_field_type(data, list)
        DataValidator.validate_list_not_empty(data)
        first_model = data[0]
        headers = self.get_class_fields(first_model)
        doc = Document()
        ss = doc.StyleSheet
        section = Section()
        doc.Sections.append(section)
        p = Paragraph(ss.ParagraphStyles.Heading1)
        class_name = type(first_model).__name__
        p.append(class_name)
        section.append(p)
        column_widths = [700*3] * len(headers)
        table = Table(*column_widths)
        header_cells = [Cell(Paragraph(header)) for header in headers]
        table.AddRow(*header_cells)
        for row in data:
            row_cells = [Cell(Paragraph(to_rtf_unicode(str(getattr(row, param, ''))))) for param in headers]
            table.AddRow(*row_cells)
        section.append(table)
        self._document = doc

    def save(self, file_name: str = 'report_data.rtf'):
        try:
            renderer = Renderer()
            save_path = file_name
            if os.path.basename(file_name) == file_name:
                save_path = os.path.join(self.settings_manager.settings.reports_path, file_name)
            with open(save_path, 'w') as f:
                renderer.Write(self._document, f)
            return True
        except Exception as e:
            self.exception = e
            return False

    def get_result_b64(self) -> str:
        if self._document is None:
            raise ValueError("No data to convert. Please create the report_data first.")
        buffer = io.StringIO()
        renderer = Renderer()
        renderer.Write(self._document, buffer)
        buffer.seek(0)
        b64_result = base64.b64encode(buffer.getvalue().encode('utf-8')).decode('utf-8')
        buffer.close()
        return b64_result




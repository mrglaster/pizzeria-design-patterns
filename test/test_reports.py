import os
import unittest
from modules.domain.report.report.complex.report_docx import ReportDOCX
from modules.domain.report.report.complex.report_rtf import ReportRTF
from modules.domain.report.report.complex.report_xlsx import ReportXLSX
from modules.domain.report.report.plain_text.report_csv import ReportCSV
from modules.domain.report.report.plain_text.report_json import ReportJSON
from modules.domain.report.report.plain_text.report_markdown import ReportMarkdown
from modules.domain.report.report.plain_text.report_xml import ReportXML
from modules.domain.report.report_format.report_format import ReportFormat
from modules.exception.bad_argument_exception import BadArgumentException
from modules.factory.report_factory.report_factory import ReportFactory
from modules.repository.measurment_unit_repository import MeasurementUnitRepository
from modules.repository.nomenclature_repository import NomenclatureRepository
from modules.service.init_service.start_service import StartService
from modules.service.managers.settings_manager import SettingsManager


class TestUtils(unittest.TestCase):
    def test_report_csv_create(self):
        service = StartService()
        service.create()
        units_repo = MeasurementUnitRepository()
        report_csv = ReportCSV()
        report_csv.create(list(units_repo.get_all().values()))
        assert report_csv.get_result() is not None

    def test_report_nomenclature_csv(self):
        service = StartService()
        service.create()
        repo = NomenclatureRepository()
        report_csv = ReportCSV()
        report_csv.create(list(repo.get_all().values()))
        assert report_csv.get_result() is not None

    def test_factory_create_instance(self):
        factory = ReportFactory()
        report_instance = factory.get_report_class_instance(ReportFormat.FORMAT_CSV)
        assert report_instance is not None
        assert isinstance(report_instance, ReportCSV)

    def test_unknown_report_format(self):
        factory = ReportFactory()
        with self.assertRaises(BadArgumentException):
            report_instance = factory.get_report_class_instance("azaza")

    def test_report_json(self):
        repo = NomenclatureRepository()
        report = ReportJSON()
        report.create(list(repo.get_all().values()))
        assert report.get_result() is not None
        assert 'Nomenclature' in report.get_result()

    def test_report_markdown(self):
        repo = NomenclatureRepository()
        report = ReportMarkdown()
        report.create(list(repo.get_all().values()))
        assert report.get_result() is not None
        assert 'nomenclature' in report.get_result()

    def test_report_xml(self):
        repo = NomenclatureRepository()
        report = ReportXML()
        report.create(list(repo.get_all().values()))
        assert report.get_result() is not None
        assert 'Nomenclatures' in report.get_result()

    def test_report_docx(self):
        repo = NomenclatureRepository()
        report = ReportDOCX()
        report.create(list(repo.get_all().values()))
        assert report.get_result() is not None

    def test_report_xlsx(self):
        repo = NomenclatureRepository()
        report = ReportXLSX()
        report.create(list(repo.get_all().values()))
        assert report.get_result() is not None

    def test_report_rtf(self):
        repo = NomenclatureRepository()
        report = ReportRTF()
        report.create(list(repo.get_all().values()))
        assert report.get_result() is not None

    def test_save_reports(self):
        repo = NomenclatureRepository()
        data = list(repo.get_all().values())

        report = ReportXML()
        report.create(data)
        report.save('report.xml')

        report = ReportCSV()
        report.create(data)
        report.save('report.csv')

        report = ReportJSON()
        report.create(data)
        report.save('report.json')

        report = ReportMarkdown()
        report.create(data)
        report.save('report.md')

        # Разделяем вызовы методов create и save
        report = ReportRTF()
        report.create(data)
        report.save('report.rtf')

        report = ReportXLSX()
        report.create(data)
        report.save('report.xlsx')

        report = ReportDOCX()
        report.create(data)
        report.save('report.docx')

        sm = SettingsManager()
        path = os.path.join(os.getcwd(), sm.settings.reports_path).replace('test/', '')

        assert len(os.listdir(path)) == 7

import os
import unittest
from src.modules.domain.report.report.complex.report_docx import ReportDOCX
from src.modules.domain.report.report.complex.report_rtf import ReportRTF
from src.modules.domain.report.report.complex.report_xlsx import ReportXLSX
from src.modules.domain.report.report.plain_text.report_csv import ReportCSV
from src.modules.domain.report.report.plain_text.report_json import ReportJSON
from src.modules.domain.report.report.plain_text.report_markdown import ReportMD
from src.modules.domain.report.report.plain_text.report_xml import ReportXML
from src.modules.domain.report.report_format.report_format import ReportFormat
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.factory.report_factory.report_factory import ReportFactory
from src.modules.repository.measurment_unit_repository import MeasurementUnitRepository
from src.modules.repository.nomenclature_repository import NomenclatureRepository
from src.modules.service.init_service.start_service import StartService
from src.modules.service.managers.settings_manager import SettingsManager


class TestReports(unittest.TestCase):
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
        report = ReportMD()
        report.create(list(repo.get_all().values()))
        assert report.get_result() is not None
        assert 'nomenclature' in report.get_result()

    def test_report_xml(self):
        repo = NomenclatureRepository()
        report = ReportXML()
        report.create(list(repo.get_all().values()))
        assert report.get_result() is not None
        assert 'Nomenclature' in report.get_result()

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
        factory = ReportFactory()
        for rep_type in ReportFormat:
            if rep_type != ReportFormat.FORMAT_ABSTRACT:
                report = factory.get_report_class_instance(rep_type)
                report.create(data)
                assert report.save()
        sm = SettingsManager()
        path = os.path.join(os.getcwd(), sm.settings.reports_path).replace('tests/', '')
        assert len(os.listdir(path)) == 7

    def test_invalid_save(self):
        service = StartService()
        service.create()
        repo = NomenclatureRepository()
        data = list(repo.get_all().values())
        report = ReportXML()
        report.create(data)
        assert not report.save('/home/azazazaza/report_data.xml')
        assert report.exception is not None
        assert isinstance(report.exception, FileNotFoundError)

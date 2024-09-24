import unittest
from modules.domain.report.report.report_csv import ReportCSV
from modules.domain.report.report_format.report_format import ReportFormat
from modules.exception.bad_argument_exception import BadArgumentException
from modules.factory.report_factory.report_factory import ReportFactory
from modules.repository.measurment_unit_repository import MeasurementUnitRepository
from modules.repository.nomenclature_repository import NomenclatureRepository
from modules.service.init_service.start_service import StartService


class TestUtils(unittest.TestCase):
    def test_report_csv_create(self):
        service = StartService()
        service.create()
        units_repo = MeasurementUnitRepository()
        report_csv = ReportCSV()
        report_csv.create('out.txt', list(units_repo.get_all().values()))
        assert report_csv.result is not None

    def test_report_nomenclature_csv(self):
        service = StartService()
        service.create()
        repo = NomenclatureRepository()
        report_csv = ReportCSV()
        report_csv.create('out.txt', list(repo.get_all().values()))
        assert report_csv.result is not None

    def test_factory_create_instance(self):
        factory = ReportFactory()
        report_instance = factory.get_report_class_instance(ReportFormat.FORMAT_CSV)
        assert report_instance is not None
        assert isinstance(report_instance, ReportCSV)

    def test_unknown_report_format(self):
        factory = ReportFactory()
        with self.assertRaises(BadArgumentException):
            report_instance = factory.get_report_class_instance("azaza")


import unittest
from datetime import datetime

from src.modules.domain.enum.filter_types import FilterType
from src.modules.domain.report.report.plain_text.report_json import ReportJSON
from src.modules.dto.tbs import TbsRequestDTO
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.repository.storage_repository import StorageRepository
from src.modules.repository.storage_transaction_repository import StorageTransactionRepository
from src.modules.service.init_service.start_service import StartService
from src.modules.service.process.tbs.tbs_process import TbsProcess


class TestTbs(unittest.TestCase):

    def test_tbs_getting_pipeline(self):
        StartService().create()
        assert len(StorageTransactionRepository.get_all().values()) == 10004
        start_date = datetime.strptime("2001-10-29 19:12:24.538308", "%Y-%m-%d %H:%M:%S.%f")
        end_date = datetime.strptime("2012-11-29 19:12:24.538308", "%Y-%m-%d %H:%M:%S.%f")
        storage_name = 'storage-name-1'
        transactions_proto = DomainPrototype()
        transactions_proto.create_from_repository("storage_transaction")
        transactions_data = (transactions_proto.
                             filter_by(field_name="transaction_time", filter_type=FilterType.GREATER_THAN,
                                       value=start_date).
                             filter_by(field_name="transaction_time", filter_type=FilterType.LESS_THAN, value=end_date).
                             filter_by("storage|name", value=storage_name, filter_type=FilterType.EQUALS).get_data())

        assert transactions_data
        dto = TbsRequestDTO(start_date=start_date, end_date=end_date, storage_name=storage_name)
        result = TbsProcess.calculate(transactions_data, False, dto)
        assert result
        assert result.opening_remainder
        assert result.remainder
        assert result.consumption
        assert result.receipt

        report = ReportJSON()
        report.create([result])
        report.save('tbs_example.json')
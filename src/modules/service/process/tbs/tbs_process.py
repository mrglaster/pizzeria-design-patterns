from src.modules.domain.enum.filter_types import FilterType
from src.modules.domain.enum.storage_types import TransactionType
from src.modules.domain.tbs.tbs_model import Tbs
from src.modules.domain.transaction.storage_transaction import StorageTransaction
from src.modules.dto.tbs import TbsRequestDTO
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.service.process.turnovers.abstract import AbstractProcess
from src.modules.service.process.turnovers.storage_turnover_all_process import StorageTurnoverProcess
from src.modules.service.process.turnovers.storage_turnover_til_higher_date_process import \
    StorageTurnoverTilHigherDateProcess


class TbsProcess(AbstractProcess):

    @staticmethod
    def calculate(data: list[StorageTransaction], add_to_repository: bool = False, *kwargs):
        request_dto: TbsRequestDTO = kwargs[0]
        proto = DomainPrototype()
        transactions_begin = (proto.create_from_repository('storage_transaction').
                              filter_by(field_name="transaction_time", filter_type=FilterType.LESS_THAN,
                                        value=request_dto.start_date).
                              filter_by(field_name="storage|name", filter_type=FilterType.EQUALS,
                                        value=request_dto.storage_name).get_data())
        opening_remainder = StorageTurnoverProcess.calculate(transactions_begin)
        remainder = StorageTurnoverTilHigherDateProcess.calculate(opening_remainder, False, request_dto.end_date, request_dto.start_date, request_dto.storage_name)
        receipt = []
        consumption = []
        for i in data:
            if i.transaction_type == TransactionType.INCOMING:
                receipt.append(i)
            else:
                consumption.append(i)
        return Tbs.create(
            opening_remainder=opening_remainder,
            remainder=remainder,
            receipt=receipt,
            consumption=consumption,
            name=f"TBS for {str(request_dto.start_date)} - {str(request_dto.end_date)}"
        )
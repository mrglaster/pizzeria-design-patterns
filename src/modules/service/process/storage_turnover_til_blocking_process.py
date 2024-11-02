from src.modules.domain.enum.filter_types import FilterType
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.service.managers.settings_manager import SettingsManager
from src.modules.service.process.abstract import AbstractProcess
from src.modules.service.process.storage_turnover_all_process import StorageTurnoverProcess


class StorageTurnoverTilBlockingDate(AbstractProcess):
    @staticmethod
    def calculate(transactions: list, add_to_repository: bool = True, **kwargs) -> list:
        blocking_date = SettingsManager().settings.blocking_date
        proto = DomainPrototype()
        proto.create(transactions)
        proto = proto.filter_by(field_name='transaction_time', filter_type=FilterType.LESS_THAN, value=blocking_date)
        trs = proto.get_data()
        return StorageTurnoverProcess.calculate(trs, add_to_repository)
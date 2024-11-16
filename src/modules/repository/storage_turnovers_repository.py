from src.modules.domain.turnover.storage_turnover import StorageTurnover
from src.modules.repository.data_repository import AbstractRepository
from src.modules.service.managers.settings_manager import SettingsManager


class StorageTurnoverRepository(AbstractRepository):
    __data = {}
    __latest_blocking_date = SettingsManager().settings.blocking_date

    @staticmethod
    def add(turnover_obj: StorageTurnover):
        key = f"{turnover_obj.uid}"
        StorageTurnoverRepository.__data[key] = turnover_obj

    @staticmethod
    def get_all():
        return StorageTurnoverRepository.__data

    @staticmethod
    def create_turnover(storage, turnover, nomenclature, measurement_unit):
        obj = StorageTurnover.create(storage=storage, turnover=turnover, nomenclature=nomenclature,
                                     measurement_unit=measurement_unit)
        StorageTurnoverRepository.add(obj)
        return obj

    @staticmethod
    def get_latest_turnovers_date():
        return StorageTurnoverRepository.__latest_blocking_date

    @staticmethod
    def clear():
        StorageTurnoverRepository.__data = {}
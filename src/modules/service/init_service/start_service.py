import os

from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.repository.measurment_unit_repository import MeasurementUnitRepository
from src.modules.repository.nomenclature_group_repository import NomenclatureGroupRepository
from src.modules.repository.nomenclature_repository import NomenclatureRepository
from src.modules.repository.recipe_repository import RecipeRepository
from src.modules.repository.storage_repository import StorageRepository
from src.modules.repository.storage_transaction_repository import StorageTransactionRepository
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService
from src.modules.service.generator.transactions_generator import TransactionsGenerator
from src.modules.service.managers.settings_manager import SettingsManager
from src.modules.service.db_service.migration_service import MigrationService
from src.modules.service.process.turnovers.storage_turnover_til_blocking_process import StorageTurnoverTilBlockingDate


class StartService:
    @staticmethod
    def __create_measurement_units():
        path_base = os.path.join(os.getcwd(), 'data').replace("src/", "")
        path_base = path_base.replace('tests/', '')
        MeasurementUnitRepository.load_units_from_json(os.path.join(path_base, 'units_data.json'))

    @staticmethod
    def __create_nomenclature_items():
        flour_group = NomenclatureGroupRepository.find_by_name("ингредиент")
        flour_unit = MeasurementUnitRepository.create_new_measurement_unit("г")
        NomenclatureRepository.create_nomenclature("Пшеничная мука", flour_group, flour_unit)

    @staticmethod
    def __create_nomenclature_groups():
        NomenclatureGroupRepository.create_new_group("ингредиент")
        NomenclatureGroupRepository.create_new_group("блюдо")
        NomenclatureGroupRepository.create_new_group("рецепт")

    @staticmethod
    def __create_recipes():
        settings_manager = SettingsManager()
        file_path = os.path.join(os.getcwd(), "configuration", "settings.json").replace("test/", "").replace('src/', '')
        settings_manager.read_settings(file_path)
        recipes_path = settings_manager.settings.recipes_path
        recipes_path = os.path.join(os.getcwd(), recipes_path).replace('tests/', '').replace('src/', '')
        for i in os.listdir(recipes_path):
            current_path = os.path.join(recipes_path, i)
            RecipeRepository.load_recipe_from_file(current_path)

    @staticmethod
    def __create_storage_transaction(use_generated=False):
        path_base = os.path.join(os.getcwd(), 'data').replace("src/", "")
        path_base = path_base.replace('tests/', '')
        StorageTransactionRepository.load_from_json_file(os.path.join(path_base, 'storage_transactions.json'))
        TransactionsGenerator.create_storage_transactions(10000, add_to_repository=True)

    def create(self):
        if SettingsManager().settings.first_run:
            self.__create_nomenclature_groups()
            self.__create_measurement_units()
            self.__create_nomenclature_items()
            self.__create_recipes()
            self.__create_storage_transaction()
            if SettingsManager().settings.use_db:
                MigrationService.do_migration()
        else:
            ObserverService.raise_event(ObservableActionType.ACTION_LOAD_DUMP, None)

    def clear(self):
        MeasurementUnitRepository.clear()
        NomenclatureGroupRepository.clear()
        NomenclatureRepository.clear()
        RecipeRepository.clear()
        StorageTransactionRepository.clear()
        StorageRepository.clear()

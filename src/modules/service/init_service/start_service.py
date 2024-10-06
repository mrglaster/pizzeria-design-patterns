import os
from src.modules.repository.measurment_unit_repository import MeasurementUnitRepository
from src.modules.repository.nomenclature_group_repository import NomenclatureGroupRepository
from src.modules.repository.nomenclature_repository import NomenclatureRepository
from src.modules.repository.recipe_repository import RecipeRepository
from src.modules.service.managers.settings_manager import SettingsManager


class StartService:
    @staticmethod
    def __create_measurement_units():
        path_base = os.path.join(os.getcwd(), 'data').replace("src/", "")
        path_base = path_base.replace('tests/', '')
        MeasurementUnitRepository.load_units_from_json(os.path.join(path_base, 'units_data.json'))

    @staticmethod
    def __create_nomenclature_items():
        # Create example nomenclature items
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
        file_path = os.path.join(os.getcwd(), "configuration", "settings.json").replace("test/", "").replace('src/','')
        settings_manager.read_settings(file_path)
        recipes_path = settings_manager.settings.recipes_path
        recipes_path = os.path.join(os.getcwd(), recipes_path).replace('tests/', '').replace('src/','')
        for i in os.listdir(recipes_path):
            current_path = os.path.join(recipes_path,  i)
            RecipeRepository.load_recipe_from_file(current_path)

    def create(self):
        self.__create_nomenclature_groups()
        self.__create_measurement_units()
        self.__create_nomenclature_items()
        self.__create_recipes()

    def clear(self):
        MeasurementUnitRepository.clear()
        NomenclatureGroupRepository.clear()
        NomenclatureRepository.clear()
        RecipeRepository.clear()
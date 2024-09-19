import os
from modules.repository.measurment_unit_repository import MeasurementUnitRepository
from modules.repository.nomenclature_group_repository import NomenclatureGroupRepository
from modules.repository.nomenclature_repository import NomenclatureRepository
from modules.repository.recipe_repository import RecipeRepository


class StartService:

    def __create_measurement_units(self):
        path_base = os.path.join(os.getcwd(), 'data')
        path_base = path_base.replace('test/', '')
        MeasurementUnitRepository.load_units_from_json(os.path.join(path_base, 'units_data.json'))

    def __create_nomenclature_items(self):
        # Create example nomenclature items
        flour_group = NomenclatureGroupRepository.find_group_by_name("ингредиент")
        flour_unit = MeasurementUnitRepository.create_new_measurement_unit("г")
        NomenclatureRepository.create_nomenclature("Пшеничная мука", flour_group, flour_unit)

    def __create_nomenclature_groups(self):
        NomenclatureGroupRepository.create_new_group("ингредиент")
        NomenclatureGroupRepository.create_new_group("блюдо")
        NomenclatureGroupRepository.create_new_group("рецепт")

    def __create_recipes(self):
        path_base = os.path.join(os.getcwd(), 'docs')
        path_base = path_base.replace('test/', '')
        RecipeRepository.load_recipe_from_file(os.path.join(path_base, 'receipt1.md'))
        RecipeRepository.load_recipe_from_file(os.path.join(path_base, 'receipt2.md'))

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
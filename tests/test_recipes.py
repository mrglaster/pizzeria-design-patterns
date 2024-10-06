import os
import unittest
from src.modules.repository.measurment_unit_repository import MeasurementUnitRepository
from src.modules.repository.nomenclature_group_repository import NomenclatureGroupRepository
from src.modules.repository.nomenclature_repository import NomenclatureRepository
from src.modules.repository.recipe_repository import RecipeRepository
from src.modules.service.init_service.start_service import StartService


class TestRecipes(unittest.TestCase):

    def test_data_create(self):
        service = StartService()
        service.create()
        assert len(MeasurementUnitRepository.get_all())
        assert len(NomenclatureGroupRepository.get_all())
        assert len(NomenclatureRepository.get_all())
        assert len(RecipeRepository.get_all())

    def test_data_import(self):
        service = StartService()
        service.clear()
        assert not len(MeasurementUnitRepository.get_all())
        assert not len(NomenclatureGroupRepository.get_all())
        assert not len(NomenclatureRepository.get_all())
        assert not len(RecipeRepository.get_all())

    def test_check_custom_recipe_fields(self):
        path = os.path.join(os.getcwd(), 'docs', 'receipt2.md')
        path = path.replace('tests/', '')
        recipe = RecipeRepository.load_recipe_from_file(path)
        assert recipe is not None
        assert recipe.name == 'ПАНКЕЙКИ НА МОЛОКЕ'
        assert len(recipe.ingredients) == 9
        assert len(recipe.steps) == recipe.step_count != 0
        assert recipe.ingredients[0].nomenclature.measurement_unit.name == 'гр'
        assert recipe.cooking_time_mins == 25

    def test_check_repeated_ingredient(self):
        path = os.path.join(os.getcwd(), 'docs', 'receipt2.md')
        path = path.replace('tests/', '')
        recipe = RecipeRepository.load_recipe_from_file(path)
        assert recipe is not None
        assert recipe.name == 'ПАНКЕЙКИ НА МОЛОКЕ'
        assert len(recipe.ingredients) == 9
        assert len(recipe.steps) == recipe.step_count != 0
        assert recipe.ingredients[0].nomenclature.measurement_unit.name == 'гр'
        assert recipe.cooking_time_mins == 25

    def test_check_repeated_step(self):
        path = os.path.join(os.getcwd(), 'docs', 'receipt2.md')
        path = path.replace('tests/', '')
        recipe = RecipeRepository.load_recipe_from_file(path)
        assert recipe is not None
        assert recipe.name == 'ПАНКЕЙКИ НА МОЛОКЕ'
        assert len(recipe.ingredients) == 9
        assert len(recipe.steps) == recipe.step_count != 0 != 9
        assert recipe.ingredients[0].nomenclature.measurement_unit.name == 'гр'
        assert recipe.cooking_time_mins == 25

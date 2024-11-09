import unittest

from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.repository.nomenclature_repository import NomenclatureRepository
from src.modules.repository.recipe_repository import RecipeRepository
from src.modules.service.domain_editing.observer.delete_validator import DeleteValidator
from src.modules.service.domain_editing.observer.exists_validator import ExistsValidator
from src.modules.service.init_service.start_service import StartService


class TestObserver(unittest.TestCase):

    def test_observer_in_use(self):
        ss = StartService()
        ss.create()
        test_nom = list(RecipeRepository.get_all().values())[0].ingredients[0].nomenclature
        validator = DeleteValidator()
        assert not validator.notify(test_nom)

    def test_observer_not_in_use(self):
        ss = StartService()
        ss.create()

        test_nom = list(RecipeRepository.get_all().values())[0].ingredients[0].nomenclature
        test_nom.name = "biba"
        validator = DeleteValidator()
        assert validator.notify(test_nom)

    def test_exists_check(self):
        ss = StartService()
        ss.create()
        test_nom = list(RecipeRepository.get_all().values())[0].ingredients[0].nomenclature
        assert ExistsValidator().notify(test_nom)

    def test_not_exists_check(self):
        nm = Nomenclature()
        nm.name = "CRAP"
        validator = ExistsValidator()
        assert not validator.notify(nm)

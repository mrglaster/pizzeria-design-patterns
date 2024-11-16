import unittest

from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.repository.recipe_repository import RecipeRepository
from src.modules.service.domain_editing.observer.observer.delete_observer import DeleteObserverHandler
from src.modules.service.domain_editing.observer.observer.update_observer import UpdateObserverHandler
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService
from src.modules.service.domain_editing.observer.service.observers_initializer import ObserverInitializer
from src.modules.service.init_service.start_service import StartService


class TestObserver(unittest.TestCase):

    def test_observer_in_use(self):
        ss = StartService()
        ss.create()
        test_nom = list(RecipeRepository.get_all().values())[0].ingredients[0].nomenclature
        validator = DeleteObserverHandler()
        assert not validator.notify(test_nom)

    def test_observer_not_in_use(self):
        ss = StartService()
        ss.create()
        test_nom = Nomenclature.create(name="biba")
        validator = DeleteObserverHandler()
        assert validator.notify(test_nom)

    def test_observers_initializer(self):
        ObserverInitializer.initialize_observers()
        assert len(ObserverService.observers)

    def test_observer_in_use_via_service(self):
        ss = StartService()
        ss.create()
        ObserverInitializer.initialize_observers()
        test_nom = list(RecipeRepository.get_all().values())[0].ingredients[0].nomenclature
        assert not ObserverService.raise_event(ObservableActionType.ACTION_DELETE, test_nom)

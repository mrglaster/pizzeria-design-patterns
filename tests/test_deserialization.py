import unittest

from src.modules.convertion.converter.json_converter import JSONConverter
from src.modules.convertion.converter.xml_converter import XMLConverter
from src.modules.repository.measurment_unit_repository import MeasurementUnitRepository
from src.modules.repository.nomenclature_repository import NomenclatureRepository
from src.modules.repository.recipe_repository import RecipeRepository
from src.modules.service.init_service.start_service import StartService


class TestRecipes(unittest.TestCase):
    def test_deserialization_from_string(self):
        data = """{
                    "name": "Сахар",
                    "uid": "fac20c1b-6fe3-47f6-8190-dedb28218403",
                    "nomenclature_group": {
                        "name": "ингредиент",
                        "uid": "3c3e84a8-4b3e-4224-b1a5-a15cd8932544"
                    },
                    "measurement_unit": {
                        "name": "гр",
                        "uid": "0d260750-e115-4b47-8eb5-5cc3f1b63693",
                        "unit": 1.0,
                        "base_measure_unit": null
                    },
                    "full_name": "nomenclature_full_name"
                }"""
        obj_instance = JSONConverter.deserialize("nomenclature", data)
        obj_reprocessed = JSONConverter.deserialize("nomenclature", JSONConverter.serialize(obj_instance))
        assert obj_reprocessed == obj_instance

    def test_compare_nomenclature_repository(self):
        service = StartService()
        service.create()
        for i in NomenclatureRepository.get_all().values():
            json_str = JSONConverter.serialize(i)
            processed = JSONConverter.deserialize('nomenclature', json_str)
            assert NomenclatureRepository.find_by_name(processed.name) == processed

    def test_compare_mu_repository(self):
        service = StartService()
        service.create()
        for i in MeasurementUnitRepository.get_all().values():
            json_str = JSONConverter.serialize(i)
            processed = JSONConverter.deserialize('measurement_unit', json_str)
            assert MeasurementUnitRepository.find_by_name(processed.name) == processed

    def test_compare_recipe_repository(self):
        service = StartService()
        service.create()

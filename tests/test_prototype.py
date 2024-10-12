import unittest
from src.modules.dto.filter_dto import FilterDTO
from src.modules.prototype.nomenclature_prototype import NomenclaturePrototype
from src.modules.repository.nomenclature_repository import NomenclatureRepository
from src.modules.service.init_service.start_service import StartService


class TestPrototype(unittest.TestCase):
    def test_prototype_nomenclature(self):
        repository = NomenclatureRepository()
        start = StartService()
        start.create()
        data = list(repository.get_all().values())
        item = data[0]
        item_filter = FilterDTO()
        item_filter.name = item.name
        prototype = NomenclaturePrototype(data)
        prototype.create(data, item_filter)
        assert len(prototype.data) == 1
        assert prototype.data[0] == item

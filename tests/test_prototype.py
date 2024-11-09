import unittest
from src.modules.domain.enum.filter_types import FilterType
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.repository.nomenclature_repository import NomenclatureRepository
from src.modules.service.init_service.start_service import StartService


class TestPrototype(unittest.TestCase):

    def test_nomenclature_prototype_equals(self):
        start_service = StartService()
        start_service.create()
        example_object_to_find = list(NomenclatureRepository().get_all().values())[0]
        prototype = DomainPrototype()
        prototype = (prototype.create_from_repository('nomenclature').
                     filter_by("name", example_object_to_find.name, FilterType.EQUALS).
                     filter_by("uid", example_object_to_find.uid, FilterType.EQUALS))
        result = prototype.get_data()
        assert result is not None
        assert len(result) == 1
        assert result[0] == example_object_to_find

    def test_nomenclature_prototype_like(self):
        prototype = DomainPrototype()
        prototype = prototype.create_from_repository('nomenclature').filter_by("name", 'ние', FilterType.LIKE)
        result = prototype.get_data()
        assert result is not None
        assert len(result) == 2

    def test_nested_parameters(self):
        StartService().create()
        prototype = DomainPrototype()
        prototype = prototype.create_from_repository("measurement_unit").filter_by("name", value="кг",
                                                                                   filter_type=FilterType.EQUALS)
        result = prototype.get_data()
        assert result
        assert len(result) == 3  # Кг, Ц, Т

    def test_prototype_chain_store(self):
        StartService().create()
        prototype = DomainPrototype().create_from_repository('nomenclature')
        prototypes = [prototype]
        lens = [len(prototype.get_data())]
        for i in 'масло':
            prototype = prototype.filter_by("name", value=i, filter_type=FilterType.LIKE)
            prototypes.append(prototype)
            lens.append(len(prototype.get_data()))
        result = prototype.get_data()
        assert len(list(set(lens))) > 2
        assert result
        for i in range(len(prototypes)):
            assert prototypes[i].get_data()
            assert len(prototypes[i].get_data()) == lens[i]

    def test_internal_fields_search(self):
        StartService().create()
        assert len(DomainPrototype().create_from_repository("storage_transaction").filter_by(
            field_name='storage|address|building_number', value="8", filter_type=FilterType.EQUALS).get_data()) == 1
        assert len(DomainPrototype().create_from_repository("storage_transaction").filter_by(
            field_name='storage|address|building_number', value="13", filter_type=FilterType.EQUALS).get_data()) == 2
        assert len(DomainPrototype().create_from_repository("storage_transaction").filter_by(
            field_name='storage|address|building_number', value="1", filter_type=FilterType.LIKE).get_data()) == 2
        assert len(DomainPrototype().create_from_repository("storage_transaction").filter_by(
            field_name='storage|address|building_number', value="228", filter_type=FilterType.EQUALS).get_data()) == 0

    def test_less_than(self):
        StartService().create()
        assert len(DomainPrototype().create_from_repository("storage_transaction").filter_by(
            field_name='amount', filter_type=FilterType.LESS_THAN,  value=30.0).get_data()) == 1

    def test_greater_than(self):
        StartService().create()
        assert len(DomainPrototype().create_from_repository("storage_transaction").filter_by(
            field_name='amount', filter_type=FilterType.GREATER_THAN,  value=30.0).get_data()) == 2
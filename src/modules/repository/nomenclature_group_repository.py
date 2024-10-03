from src.modules.domain.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.modules.repository.data_repository import AbstractRepository
from src.modules.validation.data_validator import DataValidator


class NomenclatureGroupRepository(AbstractRepository):
    __groups = {}

    @staticmethod
    def create_new_group(name: str) -> object:
        DataValidator.validate_field_type(name, str, False)
        if name not in NomenclatureGroupRepository.__groups.keys():
            group = NomenclatureGroup()
            group.name = name
            NomenclatureGroupRepository.__groups[name] = group
            return group
        return NomenclatureGroupRepository.__groups[name]

    @staticmethod
    def find_by_name(name: str):
        DataValidator.validate_field_type(name, str, False)
        try:
            return NomenclatureGroupRepository.__groups[name]
        except:
            return None

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(NomenclatureGroupRepository, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_all():
        return NomenclatureGroupRepository.__groups

    @staticmethod
    def clear():
        NomenclatureGroupRepository.__groups = {}
from src.modules.domain.measures.measurment_unit_model import MeasurementUnit
from src.modules.domain.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.repository.data_repository import AbstractRepository
from src.modules.validation.data_validator import DataValidator


class NomenclatureRepository(AbstractRepository):
    __nomenclatures = {}

    @staticmethod
    def create_nomenclature(name: str, group: NomenclatureGroup, m_unit: MeasurementUnit):
        if name not in NomenclatureRepository.__nomenclatures.keys():
            nom = Nomenclature.create(name, group, m_unit)
            NomenclatureRepository.__nomenclatures[name] = nom
            return nom
        return NomenclatureRepository.__nomenclatures[name]

    @staticmethod
    def find_by_name(name: str):
        DataValidator.validate_field_type(name, str, False)
        try:
            return NomenclatureRepository.__nomenclatures[name]
        except:
            return None

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(NomenclatureRepository, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_all():
        return NomenclatureRepository.__nomenclatures

    @staticmethod
    def clear():
        NomenclatureRepository.__nomenclatures = {}

    @staticmethod
    def add(nomenclature: Nomenclature):
        if nomenclature.name not in NomenclatureRepository.__nomenclatures:
            NomenclatureRepository.__nomenclatures[nomenclature.name] = nomenclature

    @staticmethod
    def delete(obj: Nomenclature):
        if obj.name in NomenclatureRepository.__nomenclatures:
            NomenclatureRepository.__nomenclatures.pop(obj.name)

    @staticmethod
    def update(old_object, new_object):
        if old_object.name in NomenclatureRepository.__nomenclatures:
            NomenclatureRepository.__nomenclatures[old_object.name] = new_object
            NomenclatureRepository.__nomenclatures[new_object.name] = new_object


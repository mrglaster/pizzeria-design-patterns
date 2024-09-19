from modules.domain.measures.measurment_unit_model import MeasurementUnit
from modules.domain.nomenclature.nomenclature_group_model import NomenclatureGroup
from modules.domain.nomenclature.nomenclature_model import Nomenclature
from modules.validation.data_validator import DataValidator


class NomenclatureRepository:
    __nomenclatures = {}

    @staticmethod
    def create_nomenclature(name: str, group: NomenclatureGroup, m_unit: MeasurementUnit):
        if name not in NomenclatureRepository.__nomenclatures.keys():
            nom = Nomenclature(name, group, m_unit)
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
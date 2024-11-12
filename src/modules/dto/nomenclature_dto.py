from dataclasses import dataclass

from src.modules.domain.nomenclature.nomenclature_model import Nomenclature


@dataclass
class PutNomenclatureDTO:
    nomenclature: Nomenclature


@dataclass
class UpdateNomenclatureDTO:
    uid: str
    nomenclature: Nomenclature

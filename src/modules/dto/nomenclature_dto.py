from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


class MeasurementUnitBT(BaseModel):
    name: str
    uid: str
    unit: float
    base_measurement_unit: Optional[MeasurementUnitBT]


class NomenclatureGroupBT(BaseModel):
    name: str
    uid: str


class NomenclatureBT(BaseModel):
    name: str
    uid: str
    full_name: str
    nomenclature_group: NomenclatureGroupBT
    measurement_unit: MeasurementUnitBT


@dataclass
class PutNomenclatureDTO(BaseModel):
    nomenclature: NomenclatureBT


@dataclass
class UpdateNomenclatureDTO(BaseModel):
    uid: str
    nomenclature: NomenclatureBT

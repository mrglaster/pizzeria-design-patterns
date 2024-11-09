from dataclasses import dataclass
from src.modules.domain.enum.filter_types import FilterType


@dataclass
class SingleFilter:
    field_name: str = ""
    field_value: object = None
    filter_type: FilterType = FilterType.LIKE


@dataclass
class FilterDTO:
    filters: list[SingleFilter]

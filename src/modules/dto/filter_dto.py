from dataclasses import dataclass

from src.modules.domain.enum.filter_types import FilterType
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.validation.data_validator import DataValidator


@dataclass
class SingleFilter:
    field_name: str = ""
    field_value: object = None
    filter_type: FilterType = FilterType.LIKE

@dataclass
class FilterDTO:
    filters: list[SingleFilter]
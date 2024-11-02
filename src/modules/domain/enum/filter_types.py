from enum import Enum


class FilterType(Enum):
    EQUALS = "equals"
    LIKE = "like"
    LESS_THAN = "less_than"
    GREATER_THAN = "greater_than"

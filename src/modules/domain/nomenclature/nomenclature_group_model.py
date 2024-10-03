from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.validation.data_validator import DataValidator


class NomenclatureGroup(AbstractReference):
    def __eq__(self, other):
        if not isinstance(other, NomenclatureGroup):
            return False
        return self.uid == other.uid

    def __ne__(self, other):
        return not self == other

    @classmethod
    def create(cls, name: str = "DEFAULT_NAME"):
        DataValidator.validate_field_type(name, str)
        DataValidator.validate_str_not_empty(name)
        return cls(name)

    def __str__(self):
        return self.name
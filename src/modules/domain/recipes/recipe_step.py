from __future__ import annotations
from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.validation.data_validator import DataValidator


class RecipeStep(AbstractReference):
    def __init__(self):
        super().__init__()

    @classmethod
    def create(cls, step_id = 0, description: str = "") -> RecipeStep:
        instance = cls()
        instance.step_id = step_id
        instance.step_description = description
        return instance

    @property
    def step_id(self):
        return self.__step_id

    @step_id.setter
    def step_id(self, value: int):
        DataValidator.validate_field_type(value, int)
        self.__step_id = value

    @property
    def step_description(self):
        return self.__step_description

    @step_description.setter
    def step_description(self, value: str):
        DataValidator.validate_field_type(value, str)
        self.__step_description = value

    def __eq__(self, other):
        DataValidator.validate_field_type(other, RecipeStep)
        return self.__step_id == other.step_id and self.__step_description == other.step_description

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f"{self.__step_id}: {self.step_description}"

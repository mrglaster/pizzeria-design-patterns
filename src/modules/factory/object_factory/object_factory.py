import re
from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.domain.measures.measurment_unit_model import MeasurementUnit
from src.modules.domain.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.domain.organization.organization_model import Organization
from src.modules.domain.recipes.ingredient import Ingredient
from src.modules.domain.recipes.recipe import Recipe
from src.modules.domain.recipes.recipe_step import RecipeStep
from src.modules.validation.data_validator import DataValidator


class ObjectFactory:
    __objects = {}

    def __init__(self):
        inh_children = AbstractReference.__subclasses__()
        for cls in inh_children:
            class_name = cls.__name__
            formatted_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
            self.__objects[formatted_name] = cls
            self.__objects[f"base_{formatted_name}"] = cls

    def get_object(self, object_name: str):
        DataValidator.validate_field_type(object_name, str)
        DataValidator.validate_str_not_empty(object_name)
        return self.__objects[object_name]

import re
from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.domain.measures.measurment_unit_model import MeasurementUnit
from src.modules.domain.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.domain.organization.organization_model import Organization
from src.modules.domain.recipes.ingredient import Ingredient
from src.modules.domain.recipes.recipe import Recipe
from src.modules.domain.recipes.recipe_step import RecipeStep
from src.modules.domain.storage.storage_address import Address
from src.modules.domain.storage.storage_model import Storage
from src.modules.domain.transaction.storage_transaction import StorageTransaction
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.validation.data_validator import DataValidator


class ModelDescriptionFactory:
    __objects = {}

    def __init__(self):
        inh_children = AbstractReference.__subclasses__()
        for cls in inh_children:
            class_name = cls.__name__
            formatted_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
            self.__objects[formatted_name] = cls
            self.__objects[f"base_{formatted_name}"] = cls

    def create(self, object_name: str):
        DataValidator.validate_field_type(object_name, str)
        DataValidator.validate_str_not_empty(object_name)
        shorter_name = object_name[:-1]
        if object_name not in ModelDescriptionFactory.__objects and shorter_name not in ModelDescriptionFactory.__objects:
            raise BadArgumentException(f"Unknown object name: {object_name}")
        try:
            result = self.__objects[object_name]
            return result
        except:
            result = self.__objects[shorter_name]
            return result

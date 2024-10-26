import re

from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.repository.data_repository import AbstractRepository
from src.modules.repository.measurment_unit_repository import MeasurementUnitRepository
from src.modules.repository.nomenclature_group_repository import NomenclatureGroupRepository
from src.modules.repository.nomenclature_repository import NomenclatureRepository
from src.modules.repository.recipe_repository import RecipeRepository
from src.modules.repository.storage_repository import StorageRepository
from src.modules.repository.storage_address_repository import StorageAddressRepository
from src.modules.repository.storage_transaction_repository import StorageTransactionRepository
from src.modules.service.base.abstract_logic import AbstractLogic
from src.modules.validation.data_validator import DataValidator


class RepositoryFactory(AbstractLogic):
    __repositories = {}

    def __init__(self):
        subclasses = set(list(AbstractRepository.__subclasses__()))
        for cls in subclasses:
            class_name = cls.__name__
            formatted_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower().replace("_repository", "")
            self.__repositories[formatted_name] = cls

    def get_by_name(self, name):
        DataValidator.validate_field_type(name, str, False)
        DataValidator.validate_str_not_empty(name)
        if name in self.__repositories:
            return self.__repositories[name]
        raise BadArgumentException(f"Unknown repository name: {name}")

    def set_exception(self, ex: Exception):
        pass

    @property
    def repositories(self):
        return self.__repositories
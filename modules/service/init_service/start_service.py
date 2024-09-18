from modules.domain.nomenclature.nomenclature_group_model import NomenclatureGroup
from modules.repository.data_repository import DataRepository
from modules.service.base.abstract_logic import AbstractLogic
from modules.validation.data_validator import DataValidator


class StartService(AbstractLogic):
    __repository: DataRepository = None

    def __init__(self, repository: DataRepository):
        super().__init__()
        DataValidator.validate_field_type(repository, DataRepository)
        self.__repository = repository

    def __create_nomenclature_groups(self):
        self.__repository.data[DataRepository.group_key()] = NomenclatureGroup.default_group_source(), NomenclatureGroup.default_group_production()

    def create(self):
        self.__create_nomenclature_groups()

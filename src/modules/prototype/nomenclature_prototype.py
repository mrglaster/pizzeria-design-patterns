from abc import ABC

from src.modules.dto.filter_dto import FilterDTO
from src.modules.prototype.abstract_prototype import AbstractPrototype


class NomenclaturePrototype(AbstractPrototype):

    def __init__(self, source: list):
        super().__init__(source)

    def create(self, data: list, filter_dto: FilterDTO):
        super().create(data, filter_dto)
        self.data = self.filter_name(data, filter_dto)
        self.data = self.filter_id(self.data, filter_dto)
        instance = NomenclaturePrototype(self.data)
        return instance

    def filter_name(self, source: list, filter_dto: FilterDTO) -> list:
        if filter_dto.name == "" or filter_dto.name is None:
            return source
        result = []
        for item in source:
            if item.name == filter_dto.name:
                result.append(item)
        return result

    def filter_id(self, source: list, filter_dto: FilterDTO) -> list:
        if filter_dto.id == "" or filter_dto.id is None:
            return source
        result = []
        for item in source:
            if item.name == filter_dto.id:
                result.append(item)
        return result

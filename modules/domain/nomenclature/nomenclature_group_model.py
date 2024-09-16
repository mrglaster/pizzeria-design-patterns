from modules.domain.base.abstract_reference import AbstractReference


class NomenclatureGroup(AbstractReference):
    def __eq__(self, other):
        if not isinstance(other, NomenclatureGroup):
            return False
        return self.uid == other.uid

    def __ne__(self, other):
        return not self == other
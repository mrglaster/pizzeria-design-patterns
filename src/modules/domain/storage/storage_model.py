from src.modules.domain.base.abstract_reference import AbstractReference


class Storage(AbstractReference):
    def __eq__(self, other):
        if not isinstance(other, Storage):
            return False
        return self._name == other._name

    def __ne__(self, other):
        return not self == other
from src.modules.domain.enum.filter_types import FilterType
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.service.domain_editing.domain_editing_service.crud_service import AbstractCrudService
from src.modules.service.domain_editing.observer.delete_validator import DeleteValidator
from src.modules.service.domain_editing.observer.exists_validator import ExistsValidator
from src.modules.service.domain_editing.observer.not_exists_validator import NotExistsValidator
from src.modules.service.domain_editing.observer.update_observer import UpdateObserver
from src.modules.service.domain_editing.post_processing.post_processor import PostProcessor


class NomenclatureService(AbstractCrudService):

    observers = {
        "exists": ExistsValidator(),
        "not_exists": NotExistsValidator(),
        "delete": DeleteValidator(),
        "update": UpdateObserver(),
    }

    @staticmethod
    def create(nomenclature: Nomenclature):
        existence = NomenclatureService.observers["exists"].notify(nomenclature)
        if not existence:
            PostProcessor.create(nomenclature)
            return True
        return False

    @staticmethod
    def delete(uid: str):
        nomenclature = DomainPrototype().create_from_repository("nomenclature").filter_by(field_name="uid", value=uid, filter_type=FilterType.EQUALS).first()
        if nomenclature is None:
            return False
        is_in_use = NomenclatureService.observers["delete"].notify(nomenclature)
        if is_in_use:
            return False
        PostProcessor.delete(nomenclature)
        return True

    @staticmethod
    def read(uid: str):
        nomenclature = DomainPrototype().create_from_repository("nomenclature").filter_by(field_name="uid", value=uid,
                                                                                          filter_type=FilterType.EQUALS).first()
        return nomenclature

    @staticmethod
    def update(uid: str, new_object: Nomenclature):
        new_object.uid = uid
        nomenclature = DomainPrototype().create_from_repository("nomenclature").filter_by(field_name="uid", value=uid,
                                                                                          filter_type=FilterType.EQUALS).first()
        if NomenclatureService.observers["update"].notify(nomenclature, new_object):
            PostProcessor.update(nomenclature, new_object)
            return True
        return False









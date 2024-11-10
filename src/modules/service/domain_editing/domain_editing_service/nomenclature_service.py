from src.modules.domain.enum.filter_types import FilterType
from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.service.domain_editing.domain_editing_service.crud_service import AbstractCrudService
from src.modules.service.domain_editing.observer.observer.delete_observer import DeleteObserver
from src.modules.service.domain_editing.observer.observer.update_observer import UpdateObserver
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService
from src.modules.service.domain_editing.post_processing.post_processor import PostProcessor


class NomenclatureService(AbstractCrudService):

    @staticmethod
    def create(nomenclature: Nomenclature):
        return ObserverService.raise_event(ObservableActionType.ACTION_CREATE, nomenclature)

    @staticmethod
    def delete(uid: str):
        nomenclature = DomainPrototype().create_from_repository("nomenclature").filter_by(field_name="uid", value=uid, filter_type=FilterType.EQUALS).first()
        if nomenclature is None:
            return False
        return ObserverService.raise_event(ObservableActionType.ACTION_DELETE, nomenclature)

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
        return ObserverService.raise_event(ObservableActionType.ACTION_UPDATE, nomenclature, new_object)







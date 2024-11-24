from src.modules.convertion.converter.json_converter import JSONConverter
from src.modules.domain.enum.filter_types import FilterType
from src.modules.domain.enum.observer_enum import ObservableActionType
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.dto.nomenclature_dto import PutNomenclatureDTO
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.service.domain_editing.domain_editing_service.crud_service import AbstractCrudService
from src.modules.service.domain_editing.observer.observer.delete_observer import DeleteObserverHandler
from src.modules.service.domain_editing.observer.observer.update_observer import UpdateObserverHandler
from src.modules.service.domain_editing.observer.service.observer_service import ObserverService
from src.modules.service.domain_editing.post_processing.post_processor import PostProcessor


class NomenclatureService(AbstractCrudService):

    @staticmethod
    def create(nomenclature: PutNomenclatureDTO):
        nomenclature_data = nomenclature.nomenclature.dict()
        res = JSONConverter.deserialize("nomenclature", nomenclature_data)
        return ObserverService.raise_event(ObservableActionType.ACTION_CREATE, res)

    @staticmethod
    def delete(uid: str):
        try:
            nom = DomainPrototype().create_from_repository('nomenclature').filter_by(field_name='uid', value=uid,
                                                                                     filter_type=FilterType.EQUALS).get_data()[
                0]
            if nom is None:
                return False
            return ObserverService.raise_event(ObservableActionType.ACTION_DELETE, nom)
        except:
            return False

    @staticmethod
    def read(uid: str):
        nomenclature = DomainPrototype().create_from_repository("nomenclature").filter_by(field_name="uid", value=uid,
                                                                                          filter_type=FilterType.EQUALS).first()
        return nomenclature

    @staticmethod
    def update(uid: str, new_object: PutNomenclatureDTO):
        try:
            nomenclature_data = new_object.nomenclature.dict()
            new_nomenclature = JSONConverter.deserialize("nomenclature", nomenclature_data)
            new_nomenclature.uid = uid
            nomenclature = \
            DomainPrototype().create_from_repository("nomenclature").filter_by(field_name="uid", value=uid,
                                                                               filter_type=FilterType.EQUALS).get_data()[
                0]
            return ObserverService.raise_event(ObservableActionType.ACTION_UPDATE, nomenclature, new_nomenclature)
        except:
            return False

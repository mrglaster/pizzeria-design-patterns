from src.modules.convertion.converter.abstract_converter import AbstractConverter
from src.modules.convertion.encoder.xml_encoder import XMLEncoder


class XMLConverter(AbstractConverter):

    @staticmethod
    def serialize(obj: object) -> str:
        if obj is not None:
            xml_encoder = XMLEncoder()
            return xml_encoder.encode(obj)
        return ""

    @staticmethod
    def deserialize(object_name: str, data: dict | str):
       raise NotImplementedError("This method was not implemented yet")
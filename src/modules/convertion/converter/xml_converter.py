from src.modules.convertion.converter.abstract_converter import AbstractConverter
from src.modules.convertion.encoder.xml_encoder import XMLEncoder


class XMLConverter(AbstractConverter):

    @staticmethod
    def convert(obj: object) -> str:
        if obj is not None:
            xml_encoder = XMLEncoder()
            return xml_encoder.encode(obj)
        return ""
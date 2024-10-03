import re

import xmltodict
from src.modules.convertion.converter.abstract_converter import AbstractConverter
from src.modules.convertion.converter.json_converter import JSONConverter
from src.modules.convertion.encoder.xml_encoder import XMLEncoder
from src.modules.validation.data_validator import DataValidator


class XMLConverter(AbstractConverter):

    @staticmethod
    def serialize(obj: object) -> str:
        if obj is not None:
            xml_encoder = XMLEncoder()
            return xml_encoder.encode(obj)
        return ""

    @staticmethod
    def deserialize(object_name: str, data: dict | str):
        if isinstance(data, dict):
            return JSONConverter.deserialize(object_name, data)
        DataValidator.validate_field_type(data, str)
        DataValidator.validate_str_not_empty(data)
        processed_data = re.sub(r'(?<!^)(?=[A-Z])', '_', data).lower().replace('<_', '<').replace('</_', '</')
        xml_dict = xmltodict.parse(processed_data)
        for i in xml_dict:
            if isinstance(xml_dict[i], dict):
                return JSONConverter.deserialize(i, xml_dict[i])
        return JSONConverter.deserialize(object_name, xml_dict)
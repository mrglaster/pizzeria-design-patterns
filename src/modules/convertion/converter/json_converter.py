import json
from src.modules.convertion.converter.abstract_converter import AbstractConverter
from src.modules.convertion.encoder.json_encoder import JsonEncoder


class JSONConverter(AbstractConverter):

    @staticmethod
    def convert(obj: object) -> str:
        if obj is not None:
            return json.dumps(obj, cls=JsonEncoder, indent=4, ensure_ascii=False)
        return ""

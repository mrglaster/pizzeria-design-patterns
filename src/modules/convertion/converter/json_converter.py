import json
from src.modules.convertion.converter.abstract_converter import AbstractConverter
from src.modules.convertion.encoder.json_encoder import JsonEncoder
from src.modules.validation.data_validator import DataValidator


class JSONConverter(AbstractConverter):

    @staticmethod
    def serialize(obj: object) -> str:
        if obj is not None:
            return json.dumps(obj, cls=JsonEncoder, indent=4, ensure_ascii=False)
        return ""

    @staticmethod
    def deserialize(object_name, data: dict | str):
        DataValidator.validate_field_type(object_name, str)
        DataValidator.validate_str_not_empty(object_name)
        if isinstance(data, str):
            data = json.loads(data)
        result_class = JSONConverter.objects_factory.create(object_name, )
        if hasattr(result_class, 'create') and callable(getattr(result_class, 'create')):
            instance = result_class.create()
        else:
            instance = result_class()
        for key, value in data.items():
            if hasattr(instance, key):
                if isinstance(data[key], dict):
                    c_value = JSONConverter.deserialize(key, data[key])
                elif isinstance(data[key], list):
                    c_value = [JSONConverter.deserialize(key, i) for i in data[key]]
                else:
                    c_value = value
                setattr(instance, key, c_value)

        return instance




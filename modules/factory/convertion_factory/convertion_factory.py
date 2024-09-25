from modules.service.base.abstract_logic import AbstractLogic
from modules.convertion.converter.abstract_converter import AbstractConverter
from modules.convertion.converter.json_converter import JSONConverter
from modules.convertion.converter.xml_converter import XMLConverter
from modules.exception.bad_argument_exception import BadArgumentException
from modules.validation.data_validator import DataValidator


class ConverterFactory(AbstractLogic):
    __converters = {}

    def set_exception(self, ex: Exception):
        pass

    def __init__(self):
        super().__init__()
        inh = list(AbstractConverter.__subclasses__())
        for i in inh:
            format_name = i.__name__.replace('Converter', '').lower()
            self.__converters[format_name] = i

    def convert(self, obj: object, convertion_type: str) -> str:
        DataValidator.validate_field_type(convertion_type, str)
        if convertion_type not in self.__converters:
            raise BadArgumentException(f"Convertion type not implemented: {convertion_type}")
        return self.__converters[convertion_type].convert(obj)


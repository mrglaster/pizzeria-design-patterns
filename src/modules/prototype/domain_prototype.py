import datetime

from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.domain.enum.filter_types import FilterType
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.factory.repository_factory.repository_factory import RepositoryFactory


class DomainPrototype:
    __repository_factory = RepositoryFactory()
    __data = []
    __nested_field = ""

    def create(self, data: list):
        self.__data = data
        if self.__data:
            for i in self.__data:
                if self.__init_nested_field(i):
                    break

    def __init_nested_field(self, cls_obj):
        for i in cls_obj.get_properties():
            value = getattr(cls_obj, i)
            if value.__class__ == cls_obj.__class__ and issubclass(value.__class__, AbstractReference):
                self.__nested_field = i
                return True

    def __filter_single(self, value_filter, value_source, filter_type):
        if filter_type == FilterType.EQUALS:
            return value_filter == value_source
        elif filter_type == FilterType.LIKE:
            return str(value_filter) in str(value_source)
        elif filter_type == FilterType.LESS_THAN:
            if value_filter is not None and isinstance(value_filter, datetime.datetime) and not isinstance(value_source, datetime.datetime):
                value_source = datetime.datetime.strptime(value_source, "%Y-%m-%d %H:%M:%S.%f")
            return value_source < value_filter
        elif filter_type == FilterType.GREATER_THAN:
            if value_filter is not None and isinstance(value_filter, datetime.datetime) and not isinstance(value_source, datetime.datetime):
                value_source = datetime.datetime.strptime(value_source, "%Y-%m-%d %H:%M:%S.%f")
            return value_source > value_filter
        return False

    def __get_nested_attribute(self, obj, field_path):
        fields = field_path.split("|")
        for field in fields:
            obj = getattr(obj, field, None)
            if obj is None:
                return None
        return obj

    def __check_nested_fields(self, cls_obj, property_name, value, filter_type):
        if not len(self.__nested_field):
            return False
        nested_object = getattr(cls_obj, self.__nested_field)
        if nested_object is None:
            return False
        if self.__filter_single(getattr(nested_object, property_name), value, filter_type):
            return True
        return self.__check_nested_fields(nested_object, property_name, value, filter_type)

    def create_from_repository(self, objects_name):
        repository_object = self.__repository_factory.get_by_name(objects_name)()
        self.__data = list(repository_object.get_all().values())
        if self.__data:
            for i in self.__data:
                if self.__init_nested_field(i):
                    break
        return self

    def __filter_like(self, field_name: str, value: object):
        new_data = []
        for i in self.__data:
            attribute_value = self.__get_nested_attribute(i, field_name)
            if attribute_value is not None and (
                    self.__filter_single(value, attribute_value, FilterType.LIKE)
                    or self.__check_nested_fields(i, field_name, value, FilterType.LIKE)
            ):
                new_data.append(i)
        return new_data

    def __filter_equals(self, field_name: str, value: object):
        new_data = []
        for i in self.__data:
            attribute_value = self.__get_nested_attribute(i, field_name)
            if attribute_value is not None and (
                    self.__filter_single(value, attribute_value, FilterType.EQUALS)
                    or self.__check_nested_fields(i, field_name, value, FilterType.EQUALS)
            ):
                new_data.append(i)
        return new_data

    def __filter_smaller_than(self, field_name: str, value: object):
        new_data = []
        for i in self.__data:
            attribute_value = self.__get_nested_attribute(i, field_name)
            if attribute_value is not None and isinstance(value, datetime.datetime):
                attribute_value = datetime.datetime.strptime(str(attribute_value), "%Y-%m-%d %H:%M:%S.%f")

            if attribute_value is not None and (
                    self.__filter_single(value, attribute_value, FilterType.LESS_THAN)
                    or self.__check_nested_fields(i, field_name, value, FilterType.LESS_THAN)
            ):
                new_data.append(i)
        return new_data

    def __filter_greater_than(self, field_name: str, value: object):
        new_data = []
        for i in self.__data:
            attribute_value = self.__get_nested_attribute(i, field_name)

            if attribute_value is not None and isinstance(value, datetime.datetime):
                attribute_value = datetime.datetime.strptime(attribute_value, "%Y-%m-%d %H:%M:%S.%f")

            if attribute_value is not None and (
                    self.__filter_single(value, attribute_value, FilterType.GREATER_THAN)
                    or self.__check_nested_fields(i, field_name, value, FilterType.GREATER_THAN)
            ):
                new_data.append(i)
        return new_data

    def filter_by(self, field_name: str, value: object, filter_type: FilterType):
        if not len(self.__data):
            return self
        properties = self.__data[0].get_properties()
        new_proto = DomainPrototype()

        main_field = field_name.split("|")[0]
        if main_field in properties:
            if filter_type == FilterType.LIKE:
                new_proto.create(self.__filter_like(field_name, value))
                return new_proto
            elif filter_type == FilterType.EQUALS:
                new_proto.create(self.__filter_equals(field_name, value))
                return new_proto
            elif filter_type == FilterType.LESS_THAN:
                new_proto.create(self.__filter_smaller_than(field_name, value))
                return new_proto
            elif filter_type == FilterType.GREATER_THAN:
                new_proto.create(self.__filter_greater_than(field_name, value))
                return new_proto
            return new_proto
        raise BadArgumentException(f"Unknown attribute {field_name} for class {type(self.__data[0])}")

    def get_data(self):
        return self.__data

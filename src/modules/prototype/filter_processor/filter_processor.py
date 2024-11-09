
class FilterProcessor:

    @staticmethod
    def filter_by_param(prototype, param_name, field_name, value, filter_type):
        return  prototype.filter_by(field_name=f'{param_name}|{field_name}', value=value,
                                                    filter_type=filter_type)
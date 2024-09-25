import json


import json


import json


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__dict__'):
            result_dictionary = {
                (key.split('__', 1)[1] if '__' in key else key).lstrip('_'): value
                for key, value in obj.__dict__.items()
            }
            return result_dictionary
        else:
            return super().default(obj)

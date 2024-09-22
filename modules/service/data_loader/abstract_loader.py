from modules.service.base.abstract_logic import AbstractLogic


class AbstractDataLoader(AbstractLogic):

    def set_exception(self, ex: Exception):
        pass

    @staticmethod
    def load_from_json_file(file_path):
        pass


import re
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.service.process.turnovers.abstract import AbstractProcess


class ProcessFactory:
    __processes = {}

    def __init__(self):
        subclasses = set(list(AbstractProcess.__subclasses__()))
        for cls in subclasses:
            class_name = cls.__name__
            formatted_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower().replace("_process", "")
            self.__processes[formatted_name] = cls

    @staticmethod
    def execute_process(process_name, data: list, add_to_repository: bool = False, *kwargs):
        if process_name in ProcessFactory.__processes:
            return ProcessFactory.__processes[process_name].calculate(data, add_to_repository, *kwargs)
        raise BadArgumentException(f"Unknown process name: {process_name}")

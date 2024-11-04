import re
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.service.process.abstract import AbstractProcess
from src.modules.service.process.storage_turnover_all_process import StorageTurnoverProcess
from src.modules.service.process.storage_turnover_til_blocking_process import StorageTurnoverTilBlockingDate
from src.modules.service.process.storage_turnover_til_higher_date_process import StorageTurnoverTilHigherDateProcess


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

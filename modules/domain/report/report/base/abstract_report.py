import os
from abc import ABC, abstractmethod

from modules.domain.report.report_format.report_format import ReportFormat
from modules.service.managers.settings_manager import SettingsManager
from modules.validation.data_validator import DataValidator


class AbstractReport(ABC):
    __format: ReportFormat = ReportFormat.FORMAT_ABSTRACT
    _exception: Exception = None

    @abstractmethod
    def create(self, data: list):
        pass

    @abstractmethod
    def save(self, file_name: str) -> bool:
        pass

    @abstractmethod
    def get_result(self):
        pass

    @property
    def format(self):
        return self.__format

    @property
    def exception(self):
        return self._exception

    @exception.setter
    def exception(self, e: Exception):
        DataValidator.validate_field_type(e, Exception)
        self._exception = e

    @format.setter
    def format(self, other):
        self.__format = other

    @staticmethod
    def get_class_fields(class_object: object):
        return list(filter(lambda x: not x.startswith("_") and not callable(getattr(class_object.__class__, x)),
                           dir(class_object.__class__)))


class PlainTextReport(AbstractReport, ABC):
    _result: str = ""
    _exception: Exception = None

    @property
    def result(self) -> str:
        return self._result

    def get_result(self):
        return self._result

    def save(self, file_name: str) -> bool:
        try:
            save_path = file_name
            if os.path.basename(file_name) == file_name:
                sm = SettingsManager()
                sm.read_settings()
                reps = sm.settings.reports_path
                save_path = os.path.join(reps, file_name)
            with open(save_path, 'w') as f:
                f.write(self._result)
            return True
        except Exception as e:
            self.exception = e
            return False


class ComplexReport(AbstractReport, ABC):
    _document: object = None

    def get_result(self):
        return self._document

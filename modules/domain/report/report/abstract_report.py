from abc import ABC, abstractmethod

from modules.domain.report.report_format.report_format import ReportFormat


class AbstractReport(ABC):
    __format: ReportFormat = ReportFormat.FORMAT_CSV
    __file_name: str
    _result: str = ""

    @abstractmethod
    def create(self, output_file: str, data: list):
        pass

    @property
    def result(self) -> str:
        return self._result

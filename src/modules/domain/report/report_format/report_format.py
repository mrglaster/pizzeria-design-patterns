from enum import Enum

from src.modules.exception.bad_argument_exception import BadArgumentException


class ReportFormat(Enum):
    FORMAT_CSV = 0,
    FORMAT_MARKDOWN = 1,
    FORMAT_JSON = 2,
    FORMAT_XML = 3,
    FORMAT_DOCX = 4,
    FORMAT_XLSX = 5,
    FORMAT_RTF = 6,
    FORMAT_ABSTRACT = 7

    @staticmethod
    def get_by_ordinal(ordinal: int):
        if 0 <= ordinal <= 6:
            return ReportFormat[ReportFormat.__members__.keys()[ordinal]]
        raise BadArgumentException(f"Unsupported ordinal: {ordinal}")


import datetime
from dataclasses import dataclass


@dataclass
class TurnoversDTO:
    begin_date: datetime.datetime
    end_date: datetime.datetime
    nomenclature: dict
    storage: dict

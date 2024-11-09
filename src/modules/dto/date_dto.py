import datetime
from dataclasses import dataclass


@dataclass
class GetDateDTO:
    blocking_date: datetime.datetime


@dataclass
class SetDateDTO:
    blocking_date: datetime.datetime


@dataclass
class SetDateResponseDTO:
    message: str

import datetime

from pydantic import BaseModel


class TbsRequestDTO(BaseModel):
    start_date: datetime.datetime
    end_date: datetime.datetime
    storage_name: str

from pydantic import BaseModel


class MessageDTO(BaseModel):
    status: int = 200
    detail: str = ""
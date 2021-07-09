from pydantic import BaseModel


class InputDetailsModel(BaseModel):
    url: str

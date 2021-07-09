from pydantic import BaseModel


class EventModel(BaseModel):
    title: str
    url: str
    local: str
    hours: str
    image: str
    month: str
    day: str

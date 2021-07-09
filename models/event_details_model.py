from typing import Optional
from pydantic import BaseModel


class EventDetailsModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    address: Optional[str] = None
    about: Optional[str] = None
    hours: Optional[str] = None
    local: Optional[str] = None
    image: Optional[str] = None

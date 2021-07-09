from pydantic import BaseModel


class PlaceId(BaseModel):
    city: str
    place_id: str

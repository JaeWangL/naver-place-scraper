from pydantic import BaseModel


class PlaceListingModel(BaseModel):
    place_name: str
    thumbnail_url: str
    place_id: str
    info_url: str

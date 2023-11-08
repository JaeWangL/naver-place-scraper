from pydantic import BaseModel


class PlaceInfoModel(BaseModel):
    place_name: str
    address: str
    open_time: str
    tel_number: str
    description_preview: str
    link_instagram: str

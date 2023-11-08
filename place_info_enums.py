from enum import Enum, unique

@unique
class PlaceInfoXPathsEnum(Enum):
    THUMBNAIL_MAIN = "/html/body/div[3]/div/div/div/div[1]/div/div[1]/div/a/div"
    PLACE_NAME = "/html/body/div[3]/div/div/div/div[2]/div[1]/div[1]/span[1]"

@unique
class PlaceInfoClassnamesEnum(Enum):
    ADDRESS = "LDgIH"
    TEL_NUMBER = "xlx7Q"
    OPEN_TIME_MORE = "gKP9i.RMgN0"
    OPEN_TIME_LIST = "A_cdD"
    DESCRIPTION_PREVIEW = "zPfVt"
    EXTERNAL_LINKS_CONTAINER = "O8qbU.yIPfO"


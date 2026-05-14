from pydantic import BaseModel, HttpUrl
from datetime import datetime

class CreateUrl(BaseModel):
    original_url: HttpUrl  



class GetUrl(BaseModel):
    short_code: str
    original_url: HttpUrl
    created_at: datetime 


class Statistics(GetUrl):
    clicks: int

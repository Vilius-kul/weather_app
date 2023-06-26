from typing import Optional

from pydantic import BaseModel


class Location(BaseModel):
    city: str
    region: Optional[str] = None

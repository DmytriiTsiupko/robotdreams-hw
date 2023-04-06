from pydantic import BaseModel, validator


class City(BaseModel):
    city: str



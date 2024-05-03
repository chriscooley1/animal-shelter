from pydantic import BaseModel


class AnimalCounts(BaseModel):
    cats: int
    dogs: int

class Shelter(BaseModel):
    name: str
    address: str
    animals:  AnimalCounts
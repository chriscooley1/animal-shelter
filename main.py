# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.
from fastapi import FastAPI, HTTPException

from models import Shelter, AnimalCounts

app = FastAPI()

shelters: list[Shelter] = [
    Shelter(
        name="St. George Animal Shelter",
        address="605 Waterworks Dr, St. George, UT 84770",
        animals=AnimalCounts(cats=13, dogs=15)
    ),
    Shelter(
        name="St. George Paws",
        address="1125 W 1130 N, St. George, UT 84770",
        animals=AnimalCounts(cats=12, dogs=9)
    ),
    Shelter(
        name="Animal Rescue Team",
        address="1838 W 1020 N Ste. B, St. George, UT 84770",
        animals=AnimalCounts(cats=4, dogs=7)
    )
]


@app.get("/shelters")
def get_shelters():
    return shelters

@app.get("/shelters/{shelter_id}")
def get_shelter(shelter_id: int):
    if shelter_id < 0 or shelter_id >= len(shelters):
        raise HTTPException(status_code=404, detail="Shelter not found")
    return shelters[shelter_id]

@app.post("/shelters")
def create_shelter(shelter: Shelter):
    shelters.append(shelter)
    return shelter

@app.put("/shelters/{shelter_id}")
def update_shelter(shelter_id: int, updated_shelter: Shelter):
    if shelter_id < 0:
        raise HTTPException(status_code=400, detail="Invalid shelter ID")
    if shelter_id >= len(shelters):
        # Create new shelter
        shelters.append(updated_shelter)
    else:
        # Update existing shelter
        shelters[shelter_id] = updated_shelter
    return updated_shelter

@app.delete("/shelters/{shelter_id}")
def delete_shelter(shelter_id: int):
    if shelter_id < 0 or shelter_id >= len(shelters):
        raise HTTPException(status_code=404, detail="Shelter not found")
    deleted_shelter = shelters.pop(shelter_id)
    return {"message": "Shelter deleted", "shelter": deleted_shelter}
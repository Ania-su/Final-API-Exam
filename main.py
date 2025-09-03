from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette import status
from starlette.responses import Response

app = FastAPI()

@app.get("/health")
def get_health():
    return Response(content="Ok", status_code=200, media_type="text/plain")

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier : str
    brand : str
    model : str
    characteristics : Characteristic

phones : List[Phone] = []

@app.post("/phones", status_code=status.HTTP_201_CREATED)
def create_phone(new_phone: List[Phone]):
    phones.extend(new_phone)
    return phones

@app.get("/phones")
def get_phones():
    return phones

@app.get("/phones/{phone_id}")
def get_phone(phone_id: int):
    if phone_id not in phones:
        raise HTTPException(status_code=404, detail="Phone not found")
    return phones[phone_id]
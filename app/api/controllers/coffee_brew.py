from typing import List

from fastapi import APIRouter

from repositories import CoffeeBrewRepository
from models import CoffeeBrewModel, CoffeeBrewIn


router = APIRouter(prefix="/coffee_brew")


@router.get("/", response_model=List[CoffeeBrewModel])
async def get_brews():
    return await CoffeeBrewRepository.get_all()


@router.get("/{id}", response_model=CoffeeBrewModel)
async def get_brew(id: int):
    return await CoffeeBrewRepository.get(id)


@router.post("/", response_model=CoffeeBrewModel)
async def create_brew(brew: CoffeeBrewIn):
    return await CoffeeBrewRepository.create(brew)


@router.put("/{id}", response_model=CoffeeBrewModel)
async def update_brew(id: int, brew: CoffeeBrewIn):
    return await CoffeeBrewRepository.update(id, brew)


@router.delete("/{id}", response_model=CoffeeBrewModel)
async def delete_brew(id: int):
    return await CoffeeBrewRepository.delete(id)

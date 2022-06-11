from typing import List

# Third-party imports
from fastapi import APIRouter

# Making-coffee imports
from repositories import CoffeeMakerRepository
from models import CoffeeMakerModel, CoffeeMakerIn


router = APIRouter(prefix="/coffee_maker")


@router.get("/", response_model=List[CoffeeMakerModel])
async def get_makers():
    return await CoffeeMakerRepository.get_all()


@router.get("/{id}", response_model=CoffeeMakerModel)
async def get_maker(id: int):
    return await CoffeeMakerRepository.get(id)


@router.post("/", response_model=CoffeeMakerModel)
async def create_maker(maker: CoffeeMakerIn):
    return await CoffeeMakerRepository.create(maker)


@router.put("/{id}", response_model=CoffeeMakerModel)
async def update_maker(id: int, maker: CoffeeMakerIn):
    return await CoffeeMakerRepository.update(id, maker)


@router.delete("/{id}", response_model=CoffeeMakerModel)
async def delete_maker(id: int):
    return await CoffeeMakerRepository.delete(id)

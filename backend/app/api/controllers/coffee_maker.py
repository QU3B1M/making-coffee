from typing import List

from fastapi import APIRouter, HTTPException

from app.repositories import CoffeeMakerRepository
from app.models import CoffeeMakerModel, CoffeeMakerIn


router = APIRouter(prefix='/coffee_maker')


@router.get('/', response_model=List[CoffeeMakerModel])
async def get_makers():
    return await CoffeeMakerRepository.get_all()


@router.get('/brewing_methods', response_model=List[str])
async def get_brewing_methods():
    return await CoffeeMakerRepository.get_brewing_methods()


@router.get('/{id}', response_model=CoffeeMakerModel)
async def get_maker(id: int):
    return await CoffeeMakerRepository.get(id)


@router.post('/', response_model=CoffeeMakerModel)
async def create_maker(maker: CoffeeMakerIn):
    return await CoffeeMakerRepository.create(maker)


@router.put('/{id}', response_model=CoffeeMakerModel)
async def update_maker(id: int, maker: CoffeeMakerIn):
    if await CoffeeMakerRepository.get(id):
        raise HTTPException(404, 'Coffee brew not found.')
    return await CoffeeMakerRepository.update(id, maker)


@router.delete('/{id}', response_model=CoffeeMakerModel)
async def delete_maker(id: int):
    if await CoffeeMakerRepository.get(id):
        raise HTTPException(404, 'Coffee brew not found.')
    return await CoffeeMakerRepository.delete(id)

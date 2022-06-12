from .base import BaseRepository
from models import CoffeeMakerModel
from schemas import CoffeeMaker, BrewingMethods


class CoffeeMakerRepository(BaseRepository):
    schema = CoffeeMaker
    model = CoffeeMakerModel

    @classmethod
    async def get_brewing_methods(cls) -> list:
        return BrewingMethods.list()

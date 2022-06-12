from .base import BaseRepository
from app.models import CoffeeMakerModel
from app.schemas import CoffeeMaker, BrewingMethods


class CoffeeMakerRepository(BaseRepository):
    schema = CoffeeMaker
    model = CoffeeMakerModel

    @classmethod
    async def get_brewing_methods(cls) -> list:
        return BrewingMethods.list()

from .base import BaseRepository
from app.models import CoffeeBrewModel
from app.schemas import CoffeeBrew


class CoffeeBrewRepository(BaseRepository):
    schema = CoffeeBrew
    model = CoffeeBrewModel

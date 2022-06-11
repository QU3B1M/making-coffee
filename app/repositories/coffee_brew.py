from .base import BaseRepository
from models import CoffeeBrewModel
from schemas import CoffeeBrew


class CoffeeBrewRepository(BaseRepository):
    schema = CoffeeBrew
    model = CoffeeBrewModel

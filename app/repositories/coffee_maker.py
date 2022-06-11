from .base import BaseRepository
from schemas import CoffeeBrew
from models import CoffeeBrewModel


class CoffeeBrewRepository(BaseRepository):
    schema = CoffeeBrew
    model = CoffeeBrewModel

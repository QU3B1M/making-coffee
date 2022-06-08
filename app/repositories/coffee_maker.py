from .base import BaseRepository
from schemas import CoffeeMaker
from models import CoffeeMakerModel


class CoffeeMakerRepository(BaseRepository):
    schema = CoffeeMaker
    model = CoffeeMakerModel

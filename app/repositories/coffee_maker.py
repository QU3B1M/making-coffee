from .base import BaseRepository
from models import CoffeeMakerModel
from schemas import CoffeeMaker


class CoffeeMakerRepository(BaseRepository):
    schema = CoffeeMaker
    model = CoffeeMakerModel

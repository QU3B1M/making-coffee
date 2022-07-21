from .base import BaseRepository
from app.models import UserModel
from app.schemas import User

class CoffeeMakerRepository(BaseRepository):
    schema = User
    model = UserModel


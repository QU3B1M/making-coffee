from .base import BaseRepository
from models import MakerTypeModel
from schemas import MakerType


class MakerTypeRepository(BaseRepository):
    schema = MakerType
    model = MakerTypeModel

from datetime import datetime
from enum import Enum

# Third-party imports
from tortoise import fields
from tortoise.models import Model


class Category(str, Enum):
    """Coffee Maker Possible Categories."""

    ELECTRIC = "electric"
    MANUAL = "manual"


class Brewing(str, Enum):
    """Coffee Maker Possible Brewings."""

    PRESSURE = "pressure"
    STEEPING = "steeping"
    DRIPPING = "dripping"
    BOILING = "boiling"


class CoffeeMakerType(Model):
    """Coffee Maker Types DataBase Model."""

    id: int = fields.IntField(pk=True)
    name: str = fields.CharField(max_length=255)
    description: str = fields.TextField()
    category: Category = fields.CharEnumField(Category)
    brewing: Brewing = fields.CharEnumField(Brewing)
    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)

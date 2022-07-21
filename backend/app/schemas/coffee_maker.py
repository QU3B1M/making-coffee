from datetime import datetime
from enum import Enum

from tortoise import fields
from tortoise.models import Model


class BrewingMethods(str, Enum):
    '''Coffee Maker Possible Brewings.'''

    PRESSURE = 'pressure'
    STEEPING = 'steeping'
    DRIPPING = 'dripping'
    BOILING = 'boiling'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, BrewingMethods))


class CoffeeMaker(Model):
    '''Coffee Maker DataBase Model.'''

    id: int = fields.IntField(pk=True)
    name: str = fields.CharField(max_length=255)
    description: str = fields.TextField()
    method: BrewingMethods = fields.CharEnumField(BrewingMethods)
    ratio: str = fields.CharField(max_length=255)
    grind: str = fields.CharField(max_length=255)
    img_path: str = fields.CharField(max_length=255)
    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)

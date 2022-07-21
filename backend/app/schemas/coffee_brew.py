from datetime import datetime

from tortoise import fields
from tortoise.models import Model

from .coffee_maker import CoffeeMaker


class CoffeeBrew(Model):
    '''CoffeeBrew DataBase Model.'''

    id: int = fields.BigIntField(pk=True)
    name: str = fields.CharField(max_length=255)
    description: str = fields.TextField()
    maker: CoffeeMaker = fields.ForeignKeyField(
        'models.CoffeeMaker', related_name='brews'
    )
    time: int = fields.IntField()
    roast: str = fields.CharField(max_length=255)
    coffee_grams: int = fields.IntField()
    water_cc: int = fields.IntField()
    result: str = fields.CharField(max_length=255)
    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)

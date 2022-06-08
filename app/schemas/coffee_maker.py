from datetime import datetime

# Third-party imports
from tortoise import fields
from tortoise.models import Model


class CoffeeMaker(Model):
    """CoffeeMaker DataBase Model."""

    id: int = fields.BigIntField(pk=True)
    name: str = fields.CharField(max_length=255)
    description: str = fields.TextField()
    type = fields.ForeignKeyField("models.Type", related_name="makers")
    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)

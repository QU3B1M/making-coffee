from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from schemas import CoffeeMaker, BrewingMethods


CoffeeMakerModel = pydantic_model_creator(CoffeeMaker, name="CoffeeMakerModel")


class CoffeeMakerIn(BaseModel):
    name: str
    description: str
    method: BrewingMethods
    ratio: str
    grind: str

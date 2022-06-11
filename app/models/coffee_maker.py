from tortoise.contrib.pydantic import pydantic_model_creator

# Making-cofee imports
from schemas import CoffeeMaker


CoffeeMakerModel = pydantic_model_creator(CoffeeMaker, name="CoffeeMakerModel")
CoffeeMakerIn = pydantic_model_creator(CoffeeMaker, name="CoffeeMakerIn", exclude=["id", "brews", "created_at", "updated_at"])

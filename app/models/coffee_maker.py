from tortoise.contrib.pydantic import pydantic_model_creator

# CoffeeMaker imports
from schemas import CoffeeMaker


CoffeeMakerModel = pydantic_model_creator(CoffeeMaker, name="CoffeeMakerModel")

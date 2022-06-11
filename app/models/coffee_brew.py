from tortoise.contrib.pydantic import pydantic_model_creator

# CoffeeBrew imports
from schemas import CoffeeBrew


CoffeeBrewModel = pydantic_model_creator(CoffeeBrew, name="CoffeeBrewModel")

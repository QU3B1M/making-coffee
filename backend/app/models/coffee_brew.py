from tortoise.contrib.pydantic import pydantic_model_creator

from app.schemas import CoffeeBrew


CoffeeBrewModel = pydantic_model_creator(CoffeeBrew, name="CoffeeBrewModel")
CoffeeBrewIn = pydantic_model_creator(CoffeeBrew, name="CoffeeBrewIn", exclude=["id", "maker", "created_at", "updated_at"])

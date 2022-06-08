from tortoise.contrib.pydantic import pydantic_model_creator

# Making-cofee imports
from schemas import MakerType


MakerTypeModel = pydantic_model_creator(MakerType, name="MakerTypeModel")

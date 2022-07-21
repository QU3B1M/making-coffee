from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.schemas import User


UserModel = pydantic_model_creator(User, name='UserModel')
UserIn = pydantic_model_creator(User, name='UserIn', exclude=['id', 'created_at', 'updated_at'])
UserOut = pydantic_model_creator(User, name='UserOut', exclude=['password'])

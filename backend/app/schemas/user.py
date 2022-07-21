from datetime import datetime
from enum import Enum

from tortoise import fields
from tortoise.models import Model


class UserRoles(str, Enum):
    '''User Roles.'''

    ADMIN = 'admin'
    USER = 'user'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, UserRoles))


class User(Model):
    '''User DataBase Model.'''

    id: int = fields.IntField(pk=True)
    name: str = fields.CharField(max_length=255)
    email: str = fields.CharField(max_length=255)
    password: str = fields.CharField(max_length=255)
    role: UserRoles = fields.CharEnumField(UserRoles)
    created_at: datetime = fields.DatetimeField(auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(auto_now=True)

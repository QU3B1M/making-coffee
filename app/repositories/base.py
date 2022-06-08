from typing import Generic, List, TypeVar

# Third-party imports.
from pydantic import BaseModel
from tortoise.models import Model


SchemaType = TypeVar("SchemaType", bound=Model)
ModelType = TypeVar("ModelType", bound=BaseModel)


class BaseRepository(Generic[SchemaType, ModelType]):
    """Base Repository with all the default methods to handle any CRUD."""

    schema: SchemaType
    model: ModelType

    @classmethod
    async def get(cls, **kwargs) -> ModelType:
        """Default method to Retrieve an DataBase Record"""
        return await cls.model.from_queryset_single(cls.schema.get_or_none(**kwargs))

    @classmethod
    async def filter(cls, **kwargs) -> ModelType:
        """Default method to Filter Records"""
        return await cls.model.from_queryset(cls.schema.filter(**kwargs))

    @classmethod
    async def get_all(cls) -> List[ModelType]:
        """Default method to Retrieve a List of DataBase Records."""
        return await cls.model.from_queryset(cls.schema.all())

    @classmethod
    async def create(cls, obj_in: ModelType) -> ModelType:
        """Default method to Create an DataBase Record."""
        if not isinstance(obj_in, dict):
            # Converts the object to a dict
            obj_in = obj_in.dict(exclude_unset=True)

        return await cls.model.from_tortoise_orm(await cls.schema.create(**obj_in))

    @classmethod
    async def update(cls, obj_in: ModelType, **kwargs) -> None:
        """Default method to Update an DataBase Record."""
        if not isinstance(obj_in, dict):
            # Converts the object to a dict
            update_data = obj_in.dict(exclude_unset=True)

        return await cls.schema.get(**kwargs).update(**update_data)

    @classmethod
    async def delete(cls, **kwargs) -> None:
        """Default method to Delete an DataBase Record."""
        return await cls.schema.get(**kwargs).delete()

    @classmethod
    async def exists(cls, **kwargs) -> None:
        """Default method to check if exists an DataBase Record."""
        return await cls.schema.exists(**kwargs)

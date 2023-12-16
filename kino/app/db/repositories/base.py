import uuid
from tortoise import models, exceptions

from app.core.exc import common as common_exc


class BaseRepository:
    model: models.Model

    async def get(self, **kwargs) -> list[models.Model]:
        try:
            return await self.model.filter(**kwargs)
        except exceptions.DoesNotExist as e:
            raise common_exc.NotFoundException(
                f'{self.model.__name__} not found'
            ) from e
        
    async def get_by_id(self, id: int) -> models.Model:
        try:
            return await self.model.get(id=id)
        except exceptions.DoesNotExist as e:
            raise common_exc.NotFoundException(
                f'{self.model.__name__} not found'
            ) from e
        
    async def create(self, **kwargs) -> models.Model:
        try:
            return await self.model.create(**kwargs)
        except exceptions.IntegrityError as e:
            raise common_exc.CreateException(
                'Creation failed. Details: {}'.format(e)
            ) from e
        
    async def update(self, uuid: uuid.UUID, **kwargs) -> models.Model:
        try:
            model = await self.model.get(uuid=uuid)
            await model.update_from_dict(kwargs).save()
            return model
        except exceptions.IntegrityError as e:
            raise common_exc.UpdateException(
                'Update failed. Details: {}'.format(e)
            ) from e
        except exceptions.DoesNotExist as e:
            raise common_exc.NotFoundException(
                f'{self.model.__name__} not found'
            ) from e
        
    async def delete(self, uuid: uuid.UUID) -> None:
        try:
            model = await self.model.get(uuid=uuid)
            await model.delete()
        except exceptions.IntegrityError as e:
            raise common_exc.DeleteException(
                'Deletion failed. Details: {}'.format(e)
            ) from e
        except exceptions.DoesNotExist as e:
            raise common_exc.NotFoundException(
                f'{self.model.__name__} not found'
            ) from e
        
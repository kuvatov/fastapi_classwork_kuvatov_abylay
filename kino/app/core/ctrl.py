from uuid import UUID

from app.core.exc import http as http_exc
from app.core.exc import common as common_exc


class BaseController:
    repo = None

    async def get(self, **kwargs) -> dict:
        try:
            return await self.repo.get(**kwargs)
        except common_exc.NotFoundException as e:
            raise http_exc.HTTPNotFoundException() from e
        
    async def create(self, data: dict) -> dict:
        try:
            return await self.repo.create(**data)
        except common_exc.CreateException as e:
            raise http_exc.HTTPBadRequestException() from e
        
    async def update(self, uuid: UUID, **kwargs) -> dict:
        try:
            return await self.repo.update(uuid, **kwargs)
        except common_exc.NotFoundException as e:
            raise http_exc.HTTPNotFoundException() from e
        except common_exc.UpdateException as e:
            raise http_exc.HTTPBadRequestException() from e
        
    async def delete(self, uuid: UUID) -> None:
        try:
            return await self.repo.delete(uuid)
        except common_exc.NotFoundException as e:
            raise http_exc.HTTPNotFoundException() from e
        except common_exc.DeleteException as e:
            raise http_exc.HTTPBadRequestException() from e
        
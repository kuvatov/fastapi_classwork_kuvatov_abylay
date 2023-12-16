from uuid import UUID

import fastapi as fa

from app.api.genre.ctrl import GenreController
from app.api.genre.schemas import requests, responses

genre_router = fa.APIRouter(prefix='/genre', tags=['genre'])
ctrl = GenreController()


@genre_router.get('', response_model=list[responses.GenreGet])
async def get_genres(
    params: requests.GenreGet = fa.Depends(),
):
    return await ctrl.get(**params.model_dump(exclude_none=True))


@genre_router.post('', response_model=responses.GenreGet)
async def create_genre(
    data: requests.GenreGet = fa.Body(...),
):
    return await ctrl.create(**data.model_dump())


@genre_router.patch('/{uuid}', response_model=responses.GenreGet)
async def update_genre(
    uuid: UUID,
    data: requests.GenreUpdate = fa.Body(...),
):
    return await ctrl.update(uuid=uuid, **data.model_dump(exclude_none=True))


@genre_router.delete('/{uuid}', response_model=None)
async def delete_genre(
    uuid: UUID
):
    await ctrl.delete(uuid=uuid)
    return fa.Response(status_code=204)

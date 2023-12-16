from uuid import UUID

import fastapi as fa

from app.api.person.ctrl import PersonController
from app.api.person.schemas import requests, responses


person_router = fa.APIRouter(prefix="/person", tags=["person"])
ctrl = PersonController()


@person_router.get("", response_model=list[responses.PersonGet])
async def get_persons(
   params: requests.PersonGet = fa.Depends(),
):
   return await ctrl.get(**params.model_dump(exclude_none=True))


@person_router.post("", response_model=responses.PersonGet)
async def create_person(
   data: requests.PersonCreate = fa.Body(...),
):
   return await ctrl.create(**data.model_dump())


@person_router.patch("/{uuid}", response_model=responses.PersonGet)
async def update_person(
   uuid: UUID,
   data: requests.PersonUpdate = fa.Body(...),
):
   return await ctrl.update(uuid=uuid, **data.model_dump(exclude_none=True))


@person_router.delete("/{uuid}", response_model=None)
async def delete_person(
   uuid: UUID,
):
   await ctrl.delete(uuid=uuid)
   return fa.Response(status_code=204)

from datetime import datetime, date
from typing import Optional
from uuid import UUID

from app.core.schemas import BaseModel


class PersonBase(BaseModel):
    fullname: str
    birth_date: date


class PersonAllOptional(BaseModel):
    fullname: str | None
    birth_date: date | None


class PersonCreate(PersonBase):
    pass


class PersonUpdate(PersonAllOptional):
    pass


class PersonGet(PersonAllOptional):
    uuid: UUID | None
    created_at: datetime | None
    updated_at: datetime | None

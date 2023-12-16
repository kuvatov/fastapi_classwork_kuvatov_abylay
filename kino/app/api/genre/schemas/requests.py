from datetime import datetime
from uuid import UUID

from app.core.schemas import BaseModel


class GenreBase(BaseModel):
    name: str
    description: str


class GenreAllOptional(BaseModel):
    name: str | None
    description: str | None
    uuid: UUID | None
    created_at: datetime | None
    updated_at: datetime | None


class GenreCreate(GenreBase):
    pass


class GenreUpdate(GenreAllOptional):
    pass


class GenreGet(GenreAllOptional):
    pass

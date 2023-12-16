from datetime import datetime
from uuid import UUID

from app.core.schemas import BaseModel


class GenreGet(BaseModel):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
    name: str
    description: str
    
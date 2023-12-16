from datetime import datetime, date
from uuid import UUID

from app.core.schemas import BaseModel


class PersonGet(BaseModel):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
    fullname: str
    birth_date: date

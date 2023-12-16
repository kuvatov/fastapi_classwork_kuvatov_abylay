from app.db.models import Person
from app.db.repositories.base import BaseRepository


class PersonRepository(BaseRepository):
    model = Person
    
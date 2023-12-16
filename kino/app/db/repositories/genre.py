from app.db.models import Genre
from app.db.repositories.base import BaseRepository


class GenreRepository(BaseRepository):
    model = Genre
    
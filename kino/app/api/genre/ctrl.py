from app.core.ctrl import BaseController
from app.db.repositories.genre import GenreRepository


class GenreController(BaseController):
    repo = GenreRepository()
    
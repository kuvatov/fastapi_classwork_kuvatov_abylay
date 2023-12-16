from app.core.ctrl import BaseController
from app.db.repositories.person import PersonRepository


class PersonController(BaseController):
    repo = PersonRepository()
    
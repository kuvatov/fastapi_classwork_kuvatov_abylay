from fastapi import APIRouter

from app.api.genre.routes import genre_router
from app.api.person.routes import person_router


router = APIRouter(prefix='/api')
router.include_router(genre_router)
router.include_router(person_router)

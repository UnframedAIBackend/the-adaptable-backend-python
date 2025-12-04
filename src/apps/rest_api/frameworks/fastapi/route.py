from fastapi import APIRouter
from .rest_controllers.note_rest_controller import router as note_router

router = APIRouter()

router.include_router(note_router)

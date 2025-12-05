from fastapi import APIRouter
from src.core.features.note.note_dto import NoteDto
from src.core.features.note.note_controller import NoteController
from src.core.container.container import container

class NoteRestController:
    def __init__(self) -> None:
        self.note_controller: NoteController = container.note_controller()
        
        self.router = APIRouter(prefix="/notes", tags=["notes"])
        self._setup_routes()

    def _setup_routes(self) -> None:
        self.router.add_api_route(
            "/",
            self.get_notes,
            methods=["GET"],
            response_model=list[NoteDto],
            summary="Get all notes",
        )

    async def get_notes(self) -> list[NoteDto]:
        return self.note_controller.get_notes()

note_controller = NoteRestController()
router = note_controller.router

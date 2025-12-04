from fastapi import APIRouter
from .note_dto import NoteDto

class NoteRestController:
    def __init__(self) -> None:
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
        return [
            NoteDto(id=1, content="Hello 1"),
            NoteDto(id=2, content="Hello 2"),
        ]

# Instantiate the controller and expose the router
note_controller = NoteRestController()
router = note_controller.router

from fastapi import APIRouter
from src.core.features.note.note import Note, CreateNoteDto, UpdateNoteDto
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
            response_model=list[Note],
            summary="Get all notes",
        )
        self.router.add_api_route(
            "/",
            self.create_note,
            methods=["POST"],
            response_model=Note,
            summary="Create a note",
        )
        self.router.add_api_route(
            "/{id}",
            self.get_note,
            methods=["GET"],
            response_model=Note,
            summary="Get a note by ID",
        )
        self.router.add_api_route(
            "/{id}",
            self.update_note,
            methods=["PUT"],
            response_model=Note,
            summary="Update a note",
        )
        self.router.add_api_route(
            "/{id}",
            self.delete_note,
            methods=["DELETE"],
            response_model=bool,
            summary="Delete a note",
        )

    async def get_notes(self) -> list[Note]:
        return await self.note_controller.get_notes()

    async def create_note(self, note: CreateNoteDto) -> Note:
        return await self.note_controller.create_note(note)

    async def get_note(self, id: str) -> Note:
        return await self.note_controller.get_note(id)

    async def update_note(self, id: str, note: UpdateNoteDto) -> Note:
        return await self.note_controller.update_note(id, note)

    async def delete_note(self, id: str) -> bool:
        return await self.note_controller.delete_note(id)

note_controller = NoteRestController()
router = note_controller.router

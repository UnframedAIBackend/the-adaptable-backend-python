from .note import Note, CreateNoteDto, UpdateNoteDto
from .note_repository import NoteRepository


class NoteController:

    def __init__(self, note_repository: NoteRepository):
        self.note_repository = note_repository

    async def get_notes(self) -> list[Note]:
        return await self.note_repository.find_all()

    async def create_note(self, note: CreateNoteDto) -> Note:
        return await self.note_repository.create(note.dict())

    async def get_note(self, id: str) -> Note:
        return await self.note_repository.find_by_id(id)

    async def update_note(self, id: str, note: UpdateNoteDto) -> Note:
        return await self.note_repository.update(id, note.dict())

    async def delete_note(self, id: str) -> bool:
        return await self.note_repository.delete(id)

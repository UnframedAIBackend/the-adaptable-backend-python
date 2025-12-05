from .note import Note
from .note_repository import NoteRepository


class NoteController:

    def __init__(self, note_repository: NoteRepository):
        self.note_repository = note_repository

    async def get_notes(self) -> list[Note]:
        return await self.note_repository.find_all()

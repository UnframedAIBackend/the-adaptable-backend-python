from .note import Note

class NoteController:


    def __init__(self, note_repository):
        self.note_repository = note_repository

    async def get_notes(self) -> list[Note]:
        return await self.note_repository.find_all()
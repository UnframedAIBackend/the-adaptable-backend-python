from .note_dto import NoteDto

class NoteController:
    """
    Core Note Controller.
    Handles business logic for notes.
    Framework-agnostic.
    """
    def __init__(self, note_repository):
        self.note_repository = note_repository

    async def get_notes(self) -> list[NoteDto]:
        notes = await self.note_repository.find_all()
        # Convert dicts to DTOs if repository returns dicts (SQLAlchemy mappings)
        return [NoteDto(**note) for note in notes]

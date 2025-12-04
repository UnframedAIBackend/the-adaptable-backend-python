from .note_dto import NoteDto

class NoteController:
    """
    Core Note Controller.
    Handles business logic for notes.
    Framework-agnostic.
    """

    def get_notes(self) -> list[NoteDto]:
        return [
            NoteDto(id=1, content="Hello 1 - from core controller"),
            NoteDto(id=2, content="Hello 2 - from core controller"),
        ]

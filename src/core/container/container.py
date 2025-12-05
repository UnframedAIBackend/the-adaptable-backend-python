from dependency_injector import containers, providers
from src.core.features.note.note_controller import NoteController
from src.core.features.note.note_repository import NoteRepository

class Container(containers.DeclarativeContainer):
    
    note_repository = providers.Singleton(NoteRepository)
    
    note_controller = providers.Factory(
        NoteController,
        note_repository=note_repository
    )

container = Container()

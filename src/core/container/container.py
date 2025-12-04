from dependency_injector import containers, providers
from src.core.features.note.note_controller import NoteController

class Container(containers.DeclarativeContainer):
    """
    DI Container for the application.
    """
    note_controller = providers.Singleton(NoteController)

container = Container()

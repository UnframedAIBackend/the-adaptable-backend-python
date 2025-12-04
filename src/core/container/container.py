from dependency_injector import containers, providers
from src.core.features.note.note_controller import NoteController
from src.core.features.note.note_repository import NoteRepository

class Container(containers.DeclarativeContainer):
    """
    DI Container for the application.
    """

    # Register NoteRepository as a Singleton
    note_repository = providers.Singleton(NoteRepository)

    # Register NoteController as a Singleton with dependency
    note_controller = providers.Singleton(
        NoteController,
        note_repository=note_repository
    )

# Create the container instance
container = Container()

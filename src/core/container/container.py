from dependency_injector import containers, providers
from src.core.features.note.note_controller import NoteController

class Container(containers.DeclarativeContainer):
    """
    DI Container for the application.
    """

    # Register NoteController as a Singleton
    note_controller = providers.Singleton(NoteController)

# Create the container instance
container = Container()

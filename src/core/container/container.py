from dependency_injector import containers, providers
from src.core.features.note.note_controller import NoteController

class Container(containers.DeclarativeContainer):
    
    note_controller = providers.Singleton(NoteController)

container = Container()

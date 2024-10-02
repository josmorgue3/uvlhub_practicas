from app.modules.notepad.repositories import NotepadRepository
from core.services.BaseService import BaseService


class NotepadService(BaseService):
    def __init__(self):
        super().__init__(NotepadRepository())

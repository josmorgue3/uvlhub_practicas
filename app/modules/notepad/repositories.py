from app.modules.notepad.models import Notepad
from core.repositories.BaseRepository import BaseRepository


class NotepadRepository(BaseRepository):
    def __init__(self):
        super().__init__(Notepad)

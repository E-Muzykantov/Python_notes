from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class DeleteNoteCommand(Command):
    def __init__(self, notes, id):
        self.notes = notes
        self.id = id

    def execute(self):
        self.notes.delete(self.id)

from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class CreateNoteCommand(Command):
    def __init__(self, notes, id, title, text):
        self.notes = notes
        self.id = id
        self.title = title
        self.text = text

    def execute(self):
        self.notes.create(self.id, self.title, self.text)
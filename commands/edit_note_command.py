from abc import ABC, abstractmethod


# Специальный модуль для поддержки Абстрактных базовых классов
# ABC - Абстрактный базовый класс - используется для определения интерфейса,
# необходимого для реализации классам-потомкам.

class Command(ABC):
   
    @abstractmethod
    def execute(self):
        pass


class EditNoteCommand(Command):
    def __init__(self, notes, id, title=None, text=None):
        self.notes = notes  
        self.id = id 
        self.title = title 
        self.text = text 

    def execute(self):
        
        self.notes.edit(self.id, self.title, self.text)
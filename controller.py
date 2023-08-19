import os

import text as tf 
from commands.open_notes import open_notes
from view.view import view_notes
from models.notes import Notes
from commands.create_note_command import \
    CreateNoteCommand
from commands.edit_note_command import \
    EditNoteCommand
from commands.delete_note_command import \
    DeleteNoteCommand
from commands.open_list_files import list_files


def print_menu():
    print(*tf.menu, sep='')


def controller():
    notes = Notes.get_instance()
    while True:
        print_menu()
        choice = input(tf.choice)

        if choice == '1':
            print(tf.input_id)
            id = input("> ")
            print(tf.input_title)
            title = input("> ")
            print(tf.input_text)
            text = input("> ")
            c = CreateNoteCommand(notes, id, title, text)
            c.execute()
        elif choice == '2':
            print(tf.input_id)
            id = input("> ")
            d = DeleteNoteCommand(notes, id)
            d.execute()

        elif choice == '3':
            print(tf.input_id)
            id = input("> ")
            print(tf.new_values)
            print(tf.input_title)
            title = input("> ")
            print(tf.input_text)
            text = input("> ")
            e = EditNoteCommand(notes, id, title, text)
            e.execute()
        elif choice == '4':
            view_notes(notes)

        elif choice == '5':
            print(tf.saving_to_a_file)
            file_ext = input(tf.file_ext)
            if file_ext not in ('csv', 'json', 'both'):
                print(tf.unknown_file_format)
                continue
            os.environ['file_ext'] = file_ext
            notes.save_to_file()
            print(tf.successfully_saved)

        elif choice == '6':
            list_files()

        elif choice == '7':
            open_notes()

        elif choice == '0':
            break

        else:
            print(tf.invalid_choice)
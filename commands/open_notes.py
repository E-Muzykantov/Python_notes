import os
import text as tf
from models.notes import Notes


def open_notes():
    print(tf.file_name)
    file_name = input()
    csv_file = f"{file_name}.csv"
    json_file = f"{file_name}.json"

    notes = Notes.get_instance()
    notes_list = []
    if os.path.exists(csv_file):
        notes_list = notes.load_from_file(csv_file)
    elif os.path.exists(json_file):
        notes_list = notes.load_from_file(json_file)
    else:
        print(tf.file_not_found1, {file_name}, tf.file_not_found2)

    notes.notes.extend(notes_list)
    print(tf.file_added_successfully, {file_name})
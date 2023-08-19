import os

def list_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print("Список файлов:")
    for f in files:
        print("|--", f)
# Дан абсолютный путь до файла.
# Напишите программу для вывода названия файла без расширения, названия диска и корневой папки


import os

def extract_file_info(absolute_path):
    drive = os.path.splitdrive(absolute_path)[0]
    root_folder = os.path.dirname(os.path.dirname(absolute_path))
    file_name = os.path.splitext(os.path.basename(absolute_path))[0]
    return drive, root_folder, file_name

absolute_path = "C:\\Users\\User\\Documents\\example.txt"

print(extract_file_info(absolute_path))
import shutil
import os
import pathlib
import stat

def has_hidden_attribute(file):
    return bool(os.stat(str(file)).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

def is_hidden(file):
    return file.name.startswith('.') or has_hidden_attribute(file)

def move(file, new):
    shutil.move(str(file), str(new))

def rename(files, folder, name):
    for i in range(len(files)):
        move(files[i], folder/name(files, i))
    return files

def get_folder_files(path):
    return [file for file in path.iterdir() if not file.is_dir() and not is_hidden(file)]


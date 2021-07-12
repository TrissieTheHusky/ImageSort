import tempfile
import pathlib
import filelib
import os

def make_temporary():
    f, path=tempfile.mkstemp()
    os.close(f)
    return path

def make_temporary_path(suffix):
    return pathlib.Path(make_temporary()+suffix)

def move_file_to_temporary(file):
    p=make_temporary_path(file.suffix)
    filelib.move(file, p)
    return p

def move_to_temporary(files):
    result=[]
    for file in files:
        result.append(move_file_to_temporary(file))
    return result

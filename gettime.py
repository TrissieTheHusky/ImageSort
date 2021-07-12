import os
from datetime import datetime

def creation_time(file):
    return os.path.getctime(file)

def parse(text):
    return datetime.strptime(text, '%Y:%m:%d %H:%M:%S')

def from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)

import datetime
import os
from random import randint

def ls(dir, filetype):
    files=[]
    existing_saves=os.listdir(dir)
    for fname in existing_saves:
        if fname.endswith(filetype): files.append(fname)
    return files

def wget_datetime():
    now=datetime.datetime.now()
    date_string=now.strftime("%Y-%m-%d")
    time_string=now.strftime("%H-%M")
    return date_string, time_string

def wget_clock():
    now=datetime.datetime.now()
    date_str=now.strftime('%m/%d/%y')
    # time_str=now.strftime('%I:%M %p')
    time_str=now.strftime('%I:%M:%S %p')
    return date_str, time_str

def wget_timestamp():
    now=datetime.datetime.now()
    date_string=now.strftime("%Y-%m-%d")
    time_string=now.strftime("%H-%M-%S")
    timestamp=f'{date_string}_{time_string}'
    return timestamp

def get_folders_and_files(dir):
    items=os.listdir(dir)
    folders,files=[],[]
    for str in items:
        if os.path.isdir(dir+str):
            folders.append(str)
        else:
            files.append(str)

    return folders, files








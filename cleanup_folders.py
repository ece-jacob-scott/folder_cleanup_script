# this script takes a directory that needs to be cleaned as the command line argument
# Leaves files where they are if they are not standard ie. are a folder or have numbers in the name

from os import listdir, path, rename, mkdir
from time import ctime
from sys import argv

directory = argv[1]

def HasNumbers(string:str) -> bool:
    return any(i.isdigit() for i in string)

for file_name in listdir(directory):
    try:
        file_year = ctime(path.getctime(f'{directory}{file_name}')).split(' ')[-1]
        file_ext = file_name.split('.')[-1].upper()
        if HasNumbers(file_ext) or '.' not in file_name:
            continue
        if not path.exists(f'{directory}{file_ext}_{file_year}'):
            mkdir(f'{directory}{file_ext}_{file_year}')
        rename(f'{directory}{file_name}', f'{directory}{file_ext}_{file_year}/{file_name}')
    except IndexError as error:
        continue
    except OSError as error:
        print(error)
    
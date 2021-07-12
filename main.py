import filelib
import renaming
import exif
import logging
import pathlib

def sort_by_date(files):
    files.sort(key=lambda file:exif.get_date(str(file)))

def sort_all(folder):
    files=filelib.get_folder_files(folder)
    
    print('Sorting...')
    sort_by_date(files)
        
    print('Renaming...')
    renaming.rename_to_numbers(files)
    print('Finish')

def rename_all(folder):
    files=filelib.get_folder_files(folder)

    print('Renaming...')
    renaming.rename_to_numbers(files)
    print('Finish')

def get_subdirectories(folder):
    return [path for path in folder.iterdir() if path.is_dir() and path!=folder and path!=folder.parent]

logging.getLogger('exifread').setLevel(logging.CRITICAL)

folder=pathlib.Path.home()

def str_format_columns(col_list, sep=' '):
    result=''
    spaces=lambda size, maxsize: (maxsize-size if size<maxsize else 1)
    for col, maxsize in col_list:
        result+=col+sep*spaces(len(col), maxsize)
    return result[0:-spaces(len(col_list[-1][0]), col_list[-1][1])]

def format_columns(*cols, sep=' '):
    return str_format_columns(col_list=[(str(col), size) for col, size in cols], sep=sep)

def print_columns(*cols, sep=' '):
    print(format_columns(*cols, sep=sep))

while True:
    entered=input(str(folder)+'>').split(maxsplit=1)
    cmd, par=entered[0].lower() if len(entered)>=1 else None, entered[1] if len(entered)==2 else None
    if cmd:
        if cmd=='sort':
            if par and not (folder/par).exists():
                print('Folder does not exist')
            else:
                sort_all(folder/par if par else folder)
        elif cmd=='num':
            if par and not (folder/par).exists():
                print('Folder does not exist')
            else:
                rename_all(folder/par if par else folder)
        elif cmd=='up':
            folder=folder.parent
        elif cmd=='open':
            if not par:
                print('Parameter missing')
            else:
                if (folder/par).exists():
                    folder=folder/par
                else:
                    print('Folder does not exist')
        elif cmd=='go':
            if not par:
                print('Parameter missing')
            elif pathlib.Path(par).exists():
                folder=pathlib.Path(par)
            else:
                print('Folder does not exist')
        elif cmd=='folders':
            subdirs=get_subdirectories(folder)
            print('   '.join(sd.name for sd in subdirs))
        elif cmd=='files':
            files=filelib.get_folder_files(folder)
            print('   '.join(f.name for f in files))
        elif cmd=='help':
            print('sort     sort images in this folder by date and rename them as numbers accordingly')
            print('sort <F> sort images in the <F> subfolder by date and rename them as numbers accordingly')
            print('num      rename images in this folder as numbers without changing their order')
            print('num <F>  rename images in the <F> subfolder as numbers without changing their order')
            print('up       go one folder up')
            print('go <F>   go to folder <F>')
            print('open <F> go to subfolder <F>')
            print('files    display files in this folder')
            print('folders  display subfolders of this folder')
            print('help     display help')
            print('end      quit the program')
        elif cmd=='end':
            break
        else:
            print('Invalid command. Type "help" to display the list of commands.')

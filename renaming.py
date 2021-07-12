import temp
import filelib

def number_size(num):
    return len(str(num))

def get_zero_padding_format_string(zeros):
    return '{:0'+str(zeros)+'d}'

def zero_padding(zeros, num):
    return get_zero_padding_format_string(zeros).format(num)

def file_number_name(size, number, suffix):
    return zero_padding(size, number)+suffix

def rename_to_numbers(files):
    if not files:
        return files
    folder=files[0].parent
    name_size=number_size(len(files))
    files=temp.move_to_temporary(files)
    
    return filelib.rename(files, folder, lambda files, i: file_number_name(name_size, i+1, files[i].suffix))

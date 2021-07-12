import exifread
import gettime

def get_exif(filename):
    try:
        with open(filename, 'rb') as f:
            return exifread.process_file(f)
    except:
        return None

def get_date(file):
    tags=get_exif(file)
    try:
        return gettime.parse(str(tags['EXIF DateTimeOriginal'].values))
    except:
        return gettime.from_timestamp(gettime.creation_time(file))

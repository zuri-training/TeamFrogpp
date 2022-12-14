
# from django.utils.deconstruct import deconstructible
# from django.template.defaultfilters import filesizeformat
from django.core.exceptions import ValidationError
import os


# ValidationError will be raised in case of invalid type or extension


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 1073741824:
        raise ValidationError("You cannot upload file more than 1Gb")

    elif filesize < 4096:
        raise ValidationError("You cannot upload file less than 4Kb")
    else:
        return value


def compare_size( totalfilesize, userdefinedsize):
        
    if userdefinedsize > totalfilesize:
        raise ValidationError("Total filesize cannot be lower that User defined size")

    elif (totalfilesize / userdefinedsize) > 50:
        raise ValidationError("Cannot exceed 50 filesplit")


def validate_extension(file):

    valid_file_extensions = ['.json', '.csv']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unacceptable file extension.')
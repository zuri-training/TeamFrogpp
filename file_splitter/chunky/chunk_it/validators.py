import magic
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

def validate_extension(file):
    # valid_mime_types = ['application/json','application/csv']
    # file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    # if file_mime_type not in valid_mime_types:
    #     raise ValidationError('Unsupported file type.')
    valid_file_extensions = ['.json', '.csv']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unacceptable file extension.')
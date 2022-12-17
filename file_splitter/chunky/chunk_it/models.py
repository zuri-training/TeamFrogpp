from django.db import models
from django.conf import settings
from .validators import validate_file_size, validate_extension, compare_size
from django.contrib.auth.models import User
import math

# from upload_validator import FileTypeValidator


# Create your models here.

def convert_bytes(filenum, filesize):
    if filenum == 0:
        return "0"
    elif filesize == "B":
        return filenum
    elif filesize == "KB":
        return filenum * 1024
    elif filesize == "MB":
        return filenum * math.pow(1024, 2)
    elif filesize == "GB":
        return filenum * math.pow(1024, 3)


class File_result(models.Model):
    name = models.CharField(max_length=300, default='newFile')
    file = models.FileField(upload_to='files/')
    user =  models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    created_at = models.DateTimeField(auto_now_add=True)


KILOBYTES = 'KB'
MEGABYTES = 'MB'
GIGABYTES = 'GB'

BYTES_CHOICES = [
    (KILOBYTES, 'KB'),
    (MEGABYTES, 'MB'),
    (GIGABYTES, 'GB'),
]
class Chunk_file(models.Model):
                            
#     validator = FileTypeValidator(
#     allowed_types=['application/csv','application/json'],
#     allowed_extensions=['.csv', '.json']
# )


    

    size_num = models.FloatField(null=True)


    size_string = models.CharField(max_length=10, choices=BYTES_CHOICES, default=KILOBYTES)


    file = models.FileField(upload_to='uploaded_files/', validators=[validate_file_size, validate_extension])

    # compare_size(totalfilesize, convert_bytes(size_num, size_string))

    
        
    # Check if the user defined size is higher than the total file size
    # Check if the total file split exceeds 50 


    

    JSON = ".json"
    CSV = ".csv"

    FILE_TYPE_CHOICES = [
        (JSON, 'Json'),
        (CSV, 'Csv'),
    ]
    file_type = models.CharField(max_length=50, choices=FILE_TYPE_CHOICES, default=CSV)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
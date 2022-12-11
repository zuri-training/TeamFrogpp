from django.db import models
from django.conf import settings
from .validators import validate_file_size, validate_extension
from django.contrib.auth.models import User

# from upload_validator import FileTypeValidator


# Create your models here.

class File_result(models.Model):
    name = models.CharField(max_length=300, default='newFile')
    file = models.FileField(upload_to='files/')
    # user =  models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Chunk_file(models.Model):
                            
#     validator = FileTypeValidator(
#     allowed_types=['application/csv','application/json'],
#     allowed_extensions=['.csv', '.json']
# )

    file = models.FileField(upload_to='uploaded_files/', validators=[validate_file_size, validate_extension])
    size_num = models.FloatField(null=True)

    BYTES = 'B'
    KILOBYTES = 'KB'
    MEGABYTES = 'MB'
    GIGABYTES = 'GB'

    BYTES_CHOICES = [
        (BYTES, 'B'),
        (KILOBYTES, 'KB'),
        (MEGABYTES, 'MB'),
        (GIGABYTES, 'GB'),
    ]
    size_string = models.CharField(max_length=10, choices=BYTES_CHOICES, default=BYTES)

    JSON = ".json"
    CSV = ".csv"

    FILE_TYPE_CHOICES = [
        (JSON, 'Json'),
        (CSV, 'Csv'),
    ]
    file_type = models.CharField(max_length=50, choices=FILE_TYPE_CHOICES, default=CSV)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
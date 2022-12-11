from django.forms import ModelForm
from .models import Chunk_file

class ChunkFileForm(ModelForm):
    class Meta:
        model = Chunk_file
        fields= ('file', 'size_num', 'size_string', 'file_type')
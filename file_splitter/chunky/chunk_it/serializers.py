from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Chunk_file, File_result

class Chunk_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Chunk_file
        fields = ( 'file', 'size_num', 'size_string', 'file_type')

class File_resultSerializer(serializers.ModelSerializer):
    class Meta:
        model = File_result
        fields = ( 'name', 'file', 'created_at')


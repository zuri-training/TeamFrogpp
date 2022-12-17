from .models import Chunk_file, File_result
import math
from filesplit.split import Split
import pandas as pd
import os
from pathlib import Path
from django.core.files import File
# from pprint import pprint
from pathlib import Path


def fileSplitter(ID):
    filedata = Chunk_file.objects.get(pk=ID)

    filenum = filedata.size_num

    filesize = filedata.size_string

    filename = filedata.file.name
    
    

    userDefined_filetype = filedata.file_type

    filepath = 'media/{}'.format(filename)


    totalfile_size = os.path.getsize(filepath)

    filename_ext = Path(filepath).stem
    #Converting the filesize specified by the user to bytes
    ext = os.path.splitext(filepath)[-1]
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

    #Converting to a different filetype by the user request

    if userDefined_filetype != os.path.splitext(filepath)[-1].lower():

        if userDefined_filetype == '.csv':
            df = pd.read_json (filepath)
            df.to_csv (filepath, index = None)
            filename = os.path.splitext(filepath)[0] + '.csv'

        elif userDefined_filetype == '.json':
            df = pd.read_csv (filepath)  
            df.to_json (filepath)
            filename = os.path.splitext(filepath)[0] + '.json'
    # Split the data using size specified and save it to the media directory
    split= Split(filepath, "chunk_it/fileSplit/")


    hsd = math.ceil(convert_bytes(filenum, filesize))

    counter = math.ceil(totalfile_size / hsd)

    split.bysize(hsd)


    # Passing the newly created file through the model so Django has track of them
    list_ID = []
    while counter != 0 :
        path = Path('chunk_it/fileSplit/{}_{}{}'.format(filename_ext,counter,ext))
        newObject = File_result.objects.create(name="{}{}{}".format(filename_ext,counter,ext))
        with path.open(mode='rb') as f:
            newObject.file = File(f, name=path.name)
            newObject.save()
            list_ID.append(newObject.file.name)
            counter -= 1

    return list_ID
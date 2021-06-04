#!/usr/bin/env python
# coding: utf-8

# In[1]:


import audio_metadata as am
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import os
from collections import namedtuple
import json


# In[2]:


from glob import glob

#Accesing the folder
data_dir = '/Users/goundosidibe/Documents/projects/co-opts/BE'
#only select files that ends with mp3
audio_files= glob(data_dir + '/*.mp3')

#the total number of files that ends with mp3
len(audio_files)


# In[3]:


for file in range(0, len(audio_files), 1):
    metadata = am.load(audio_files[file])
   
    # extracting the metadata from the mp3 files
    data_dict = {

        "database":"Tatoeba" ,

        "source": "Tatoeba",

        "format": "mp3",

        "audio_file_name":metadata.tags.comment[0].text +".mp3",

        "audio_path": '/mnt/big-drive-2001-gp3/data/Tateoba/tatoeba_audio_eng/audio/BE',

        "transcript": metadata.tags.title,

        "aligned":True ,

        "sampling": metadata.streaminfo.sample_rate,

        "recording_device": "unknown",

        "bitrate": metadata.streaminfo.bitrate,

        "channels": metadata.streaminfo.channels,

        "precision":"none",

        "encoding": "none",

        "date": metadata.tags.date,

        "age": "unknown",

        "gender": "Male",

        "accent": "British English",

        "country": "UK",

        "region": "none",

        "user_name": "BE"

    }
    
    
        #saving the mp3 metadata info to a json file
    json_object = json.dumps(data_dict, indent = 4) 

    with open(metadata.tags.comment[0].text +".json", "x") as outfile: 
        outfile.write(json_object)

    


# In[ ]:





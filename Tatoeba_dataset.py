#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from glob import glob
import csv
import eyed3 
from pathlib import Path
import os
from csv import DictWriter
import re

# In[ ]:


p = Path("output.csv")
if p.exists():
    os.remove(p)


# In[ ]:


data_dir = '/mnt/big-drive-2001-gp3/data/Tateoba/tatoeba_audio_eng/audio/'


# In[ ]:
with open('output.csv', 'w') as csv_file:
    fieldnames = [
        "database", "source", "format", "audioFileName", "audioPath", "transcript",
        "aligned", "sampling", "recording_device", "bitrate", "channels", "precision", "encoding", "date",
        "age", "gender", "accent", "country", "region", "user_name"]
    csvwriter = csv.writer(csv_file, delimiter=",")
    csvwriter.writerow(fieldnames)


# In[ ]:

def transcript_regex_filter(transcript):  # take a transcript snippet and make it match the regex [a-z ]+
    text = re.sub("[^a-z ]+", "", transcript.lower())
    return text


def import_data(folder, speaker_gender, speaker_accent, speaker_country, speaker_region,user_name):
    audio_files = glob(data_dir +folder + '/*.mp3')
    for file in range(0, len(audio_files), 1):
        try:
            audiofile = eyed3.load(audio_files[file])
            dict = {
                'database':'Tatoeba',
                    'source': 'Tatoeba',
                    'format': 'mp3',
                   'audioFileName': Path(audio_files[file]).name,
                   'audioPath': 'tatoeba_audio_eng/audio/' + folder,
                   'transcript': transcript_regex_filter(audiofile.tag.title),
                   'aligned': True,
                   'sampling': audiofile.info.sample_freq,
                   'recording_device': 'unknown',
                    'bitrate': audiofile.info.bit_rate[1] * 1000,
                    'channels': '1',
                    'precision': 'unknown',
                    'encoding': 'unknown',
                    'date': 'unknown',
                    'age': 'unknown',
                    'gender': speaker_gender,
                    'accent': speaker_accent,
                    'country': speaker_country,
                    'region': speaker_region,
                    'user_name': user_name
                }
            
            # Open your CSV file in append mode
            # Create a file object for this file
            with open('output.csv', 'a') as f_object:
                # Pass the file object and a list 
                # of column names to DictWriter()
                # You will get a object of DictWriter
                fieldnames = [
                    "database", "source", "format", "audioFileName", "audioPath", "transcript",
                    "aligned", "sampling", "recording_device", "bitrate", "channels", "precision", "encoding", "date",
                    "age", "gender", "accent", "country", "region", "user_name"]

                dictwriter = csv.DictWriter(f_object, fieldnames=fieldnames)
                dictwriter.writerow(dict)
                #Close the file object
                f_object.close()
                
        except Exception as e:
            print(e)

            


# In[ ]:

#traversing through the files
# import for all folders
import_data("BE","Male","English","British Accent","UK","BE")
print('BE')


import_data('CK', "Male", "American English", "US", "unknown","CK")
print("CK ")

import_data("Delian", "Female", "American English", "US", "California","Delian")
print("Delian")

import_data("Susan1430", "Female", "British English", "UK", "unknown","Susan1430")
print("Susan1430")

import_data("pencil", "Female", "English", "unknown", "unknown","pencil")
print("pencil")

import_data("rhys_mcg", "Male", "Australian English", "Australia", "none","rhys_mcg")
print("rhys_mcg")


# In[ ]:

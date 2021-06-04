#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pydub
import glob
import shutil
from pathlib import Path


# In[2]:


my_dir = Path('/Users/goundosidibe/Documents/projects/co-opts/opus')

p = Path('/Users/goundosidibe/Documents/projects/co-opts/opus/wav/')


# In[3]:

#creates a log file
log = open("log.txt", "w")
total=[]
#traverse all the folder/ recursive glob
for item in my_dir.glob('**/*'):
    # transforms the opus files into wav files
    if item.suffix in ['.opus']:
            wav_file = os.path.splitext(item)[0] + '.wav'
            sound = pydub.AudioSegment.from_file(item)
            sound.export(wav_file, format="wav")
            #converting the item into string and added to the total list
            total.append(str(item))
            #adding the items to the log file
            log.write("files: %s" % (item))
            log.write("\n")
            #once the file is converted to wav , moved to a different directory
            for file in my_dir.glob('**/*'):
                try:
                    if file.suffix in ['.wav']:
                        h= os.path.join(my_dir,file)
                        shutil.move(h,p)
                except Exception:
                    pass

total = len(total) 
log.write("Total converted files: %s" % (total))
log.close()



       


# In[4]:


# import glob, os
# import shutil
# for file in my_dir.glob('**/*'):
#      if file.suffix in ['.wav']:
# #         shutil.move(os.path.join(my_dir,file),p)
#         try:
#              h= os.path.join(my_dir,file)
#              shutil.move(h,p)
#         except Exception:
#                 pass
            


# In[ ]:

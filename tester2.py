import os
import string

my_directory='Users/marilyn/Desktop/test'

for object in os.listdir(my_directory):
      if os.path.isfile(os.path.join(my_directory, object)):
              req_file=object
              ren_file=req_file.replace(‘.jpg′, ‘.mp3′)
              old_file=os.path.join(my_directory, req_file)
      		  new_file=os.path.join(my_directory, ren_file
               os.rename(old_file, new_file)

import os
from sys import argv
script,dirname, extensionToReplace, newExtension = argv
files = os.listdir(dirname)
extensionToReplace = extensionToReplace.lower()
for file in files:
    if(file.lower().endswith(extensionToReplace)):
        full_path_of_file = os.path.join(dirname, file)
        first,mid,last = full_path_of_file.rpartition('.')
        newfile = first + mid + newExtension
        print newfile
        print "renaming %s to %s" %(full_path_of_file, newfile)
        os.rename(full_path_of_file, newfile)

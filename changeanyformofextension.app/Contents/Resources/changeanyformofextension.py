import os
from sys import argv
script,dirname, extensionToReplace, newExtension = argv
files = os.listdir(dirname)
extensionToReplace = extensionToReplace.lower()
for file in files:
    if(file.lower().endswith(extensionToReplace)):
        first,mid,last = file.rpartition('.')
        newfile = first + mid + newExtension
        print newfile
        print "renaming %s to %s" %(file, newfile)
        # os.rename(file, newfile)
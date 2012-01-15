import os
from sys import argv
script,filename,ext1 = argv

files = os.listdir(os.curdir)
for file in files:
    first,mid,last = filename.rpartition('.')
    extension = last
    if extension in file:
        lower_case_extension = last.lower()
        complete_filename =  first + mid + lower_case_extension
        newfile = file.replace(extension, ext1)
        print complete_filename
        print "renaming %s to %s" %(file, newfile)
        os.rename(file, newfile)
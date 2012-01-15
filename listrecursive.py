import os
from sys import argv
script,filename = argv
filelist = []
rootdir = argv[1]
for root,subfolders,files in os.walk(rootdir):
	for file in files:
		filelist.append(os.path.join(root,file))
print filelist
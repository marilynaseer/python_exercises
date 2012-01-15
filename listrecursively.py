import os
import sys
filelist = []
rootdir = sys.argv[1]
for root,subfolders,files in os.walk(rootdir):
	for file in files:
		filelist.append(os.path.join(root,file))
print filelist
import fnmatch
import os,sys
rootpath = sys.argv[1]      
pattern = '*.txt'
if not os.path.exists(rootpath) or os.path.isfile(rootpath):
	print "no such directory exists,enter a valid directory"
else:
	for root, dirs, files in os.walk(rootpath):
		for filename in fnmatch.filter(files,pattern):
			print(os.path.join(root,filename))



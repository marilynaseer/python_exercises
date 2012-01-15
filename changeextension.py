import os,sys
from sys import argv
a = len(argv)
if a > 3:
	print "pass only two parameter"
elif a < 3:
	print "pass atleast two parameters,two valid filenames"
else :
	script ,ext1 ,ext2 = argv
	files = os.listdir(os.curdir)
	for file in files:
		if ext1 in file:
			newfile = file.replace(ext1,ext2)
			os.rename(file, newfile)
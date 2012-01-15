import os
from sys import argv
a = len(argv)
if a > 3:
	print "pass only two parameter"
elif a < 3:
	print "pass atleast two parameters,two valid filenames"
else :
	script,file1,file2 = argv
	if not os.path.isfile(file1):
		print "no such file"
	else:
		os.rename(file1,file2)

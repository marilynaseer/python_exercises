import os,sys
path = sys.argv[1]
if not os.path.exists(path) or os.path.isfile(path):
	print "no such directory exists,enter a valid directory"
else:
	os.chdir(path)
	for files in os.listdir("."):
		if files.endswith(".txt"):
			print files
		
	
		
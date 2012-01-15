import os, sys
path = sys.argv[1]
if not os.path.exists(path) or os.path.isfile(path):
	print "does not exist,enter a valid directory"
else:
	files = os.listdir(path)
 	print files
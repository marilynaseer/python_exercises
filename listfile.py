from sys import argv
script,path = argv
dirlist = listdir(path)
for fname in dirlist:
	print fname
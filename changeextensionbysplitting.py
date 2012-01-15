import os,sys
dir = sys.argv[1]
files = os.listdir(dir)
for file in files:
    full_path_of_file = os.path.join(dir, file)
    if sys.argv[2] in file:
        newfile = full_path_of_file.replace(sys.argv[2], sys.argv[3])
        print "renaming %s to %s" %(file, newfile)
        os.rename(full_path_of_file, newfile)
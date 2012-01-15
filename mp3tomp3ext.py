import sys
import os

cur_dir = sys.argv[1]
old_ext = sys.argv[2]
new_ext = sys.argv[3]

#print cur_dir, old_ext, new_ext
for root, dirs, files in os.walk(cur_dir):  
    for filename in files:  
    	file_ext = os.path.splitext(filename)[1]

    	if old_ext == file_ext:  
    		oldname = os.path.join(root, filename)  
    		newname = oldname.replace(old_ext, new_ext)  
    		os.rename(oldname, newname)

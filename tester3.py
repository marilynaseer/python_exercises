import os
files1 = os.listdir(os.curdir)
for file in files1:
    if '.jpg' in file:
        newfile = file.replace('.jpg', '.mp3')
        os.rename(file, newfile)

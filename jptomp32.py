import os,glob,sys
os.chdir(sys.argv[1])
for fi in glob.glob("*.pnt"):
   os.rename(fi, fi[:-3] + "txt")     

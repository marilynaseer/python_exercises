import os,glob
os.chdir(os.curdir)
for fi in glob.glob(".jpg"):
	os.rename(fi,fi[:-3] + ".mp3")
import os,sys
for root,dirs,files in os.walk(sys.argv[1]):
	for file in files:
			print file
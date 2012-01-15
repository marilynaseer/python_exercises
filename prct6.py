from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" %(from_file,to_file)

input = open(from_file)
indata = input.read()

print "the input file is %d bytes long"%len(indata)

print "does file exist? %r"%exists(to_file)

output = open(to_file,'w')
output.write(indata)

output.close()
input.close()
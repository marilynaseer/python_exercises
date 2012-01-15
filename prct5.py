from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "copying from %s to %s"% (from_file,to_file)

input = open(from_file)
indata = input.read()

print " the input file %d bytes long"len
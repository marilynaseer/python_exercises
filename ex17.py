from sys import argv
from os.path import exists

script,from_file,to_file=argv

print "copying from %s to %s" %(from_file,to_file)

input=open(from_file)
indata=input.read()

print "input file is %d bytes long" %len(indata)

print "does the output file exist ? %r"% exists(to_file)
print "ready hit return to continue,ctrl+c to abort"
raw_input()

output=open(to_file,'w')
output.write(indata)

print "done"

output.close()
input.close()
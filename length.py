from sys import argv 
a = len(argv)
if a > 2:
	print "pass only one parameter"
else:
	script,string = argv
	print argv 
	length = len(string)
	print "the length of string is %r" % length
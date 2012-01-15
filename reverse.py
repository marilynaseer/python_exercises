from sys import argv
a = len(argv)
if a > 2:
	print "pass only one parameter"
elif a < 2:
	print "pass atleast one parameter"
else:
	script,s = argv
	print argv
	s = s[::-1]
	print s
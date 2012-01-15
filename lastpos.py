from sys import argv
a = len(argv)
if a > 3:
	print "pass only two parameter"
elif a < 3:
	print "pass atleast two parameters,a character and a string"
else :
	script,string,str1 = argv
	print argv
	a = string.rfind(str1)
	if a >= 0:
		print "found"
		print a
	else:
		print "char  not found"
from sys import argv
a = len(argv)
if a > 3:
	print "pass only two parameter"
elif a < 3:
	print "pass atleast two parameters,a string and a character"
else:
	script,string,str1 = argv
	print argv
	a = string.find(str1)
	if  a >= 0:
		print "found" 
		print a
	else:
		found = 0
		print "char not found"
	

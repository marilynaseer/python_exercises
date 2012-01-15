from sys import argv
a = len(argv)
if a > 3:
	print"pass  only two  parameters"
elif a < 3:
	print"pass atleast two parameter"
else:
	script,string,str1 = argv
	print argv
	first,mid,last = string.rpartition(str1)
 	result = last.lower()
	res = first ,result
	print res
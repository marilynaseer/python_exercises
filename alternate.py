from sys import argv
string = argv[1]
count = 0
result = ""
for character in string:
	count +=1
	if(count % 2 == 0):
		result += character.upper()
	else:
		result += character.lower()
		
print result
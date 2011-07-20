#def reverse(str):
#	if len(str)==1:
#		revstr=str
#	else:
#		revstr=reverse(str[1:])+str[0]
		
#	return revstr
line = raw_input("input the line to reverse")

length = len(line)
	
while(length > 0):
	reversed  += line[length - 1]
	length =length -1
		
print reversed;
raw_input()
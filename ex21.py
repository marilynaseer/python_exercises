def add(a,b):
		print "adding %d+%d"% (a,b)
		return a+b
		
def subtract(a,b):
		print "subtracting %d-%d"%(a,b)
		return a-b
	
def multiply(a,b):
	print "multiply %d * %d"% (a,b)
	return a*b

def divide(a,b):
	print"dividin %d/%d"%(a,b)
	return a/b
	
print "lets do some with funcs"

age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print "age:%d,height:%d,weight:%d,iq:%d"%(age,height,weight,iq)

print "here is a puzzle"

what=add(age,subtract(height,multiply(weight,divide(iq,2))))

print "that becomes:",what,
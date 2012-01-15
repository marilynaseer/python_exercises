print "practise"
print "you\'d do tabs \t and \\ escape and newline \n"

poem ="""
\thello world 
everybody alrite
"""
print '-'* 20
print poem

five = 20+10-15-10
print "five ",five

def secret_formula(started):
	peanut = started * 10
	jars = peanut / 1000
	crates = jars / 100
	return peanut, jars, crates

start_point = 10000
peanut,jars,crates = secret_formula(start_point)

print "start point %d"% start_point
print "peanut=%d,jars=%d,crates=%d" % (peanut,jars,crates)

start_point = start_point / 10
print " peanut %d,jars %d,crates %d" % secret_formula(start_point)
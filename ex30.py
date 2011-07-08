people =10
cars =40
buses=15

if cars >people and not(people >buses):
	print "we should take the cars and not bus"
elif cars<people:
	print "we should not take the cars"
else:
	print "we can't decide"
	
if  buses >cars:
	print "too many buses"
elif buses<cars:
	print "maybe take buses"
else:
	print "we still can't decide"
if people>buses:
	print"just take buses"
else:print"forget it"
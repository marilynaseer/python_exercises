print "you enter a dark room with two doors.do you go through door #1 or door #2"

door = raw_input(">")

if door == "1":
	print "there's a giant bear here eating a cheesecake"
	print "1.take the cake"
	print "2.scream at the bear"
	
	bear = raw_input(">")
	
	if bear == "1":
		print"the bear eats your face off"
	elif bear =="2":
		print "the bear eats your legs off"
	else:
		print "well,doing %s is probably better"%bear
		
elif door == "2":
	print "you enter a wonderland"
	print "1:butterflies"
	print "2:chocolates"
	print "3:oldman"
	
	awesome=raw_input(">")
	
	if awesome== "1"or awesome =="2":
		print "you have an awesome time"
	else:
		print "you are bored to death"
else:
	print "you get scared and run away"
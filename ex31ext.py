print"you wanna go on a trip.you wanna go to place#1 or place#2"

place=raw_input("<")
if place=="1":
	print "you will be going to the amazon"
	print "1.you stay at the hotel"
	print "2.you will hav a wild adventure"
	
	trip=raw_input("<")
	
	if trip=="1":
		print "you will get bored but you will be safe"
	elif trip=="2":
		print "you will have a hell of a time but mite get eaten by an anaconda"
	else:
		print "well then you can go to some other place"
elif place=="2":
	print "you are going to hawaii"
	print "1.you will have an awesome time at the beach"
	print "2.you will have a lot of mocktails and cocktails"
	
	island=raw_input("<")
	
	if island=="1" or island=="2":
		print "you will never forget this experience"
	else:
		print "you are a borin person"
		
else:
	print"you are dumb"
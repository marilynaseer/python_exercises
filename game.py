from sys import exit

def land():
	print "you can have a lot of fun,which house do you go"
	next = raw_input(">")
	if next == '1':
		print "you go to jeena's home"
		jeena_home()
	elif next == '2':
		print "you go to ansi's home "
		ansi_home()
	else:
		print "you go to synthia's home"
		synthia_home()


def jeena_home():
	print "you gotta wait for sometime coz she mite be bathing"
	print"you want to wait or move on"
	next = raw_input(">")
	if next == 'wait':
		print "hahahaha you are dead"
	elif next == 'm running outta here':
		print "phew,that was a close one"
	else:
		print "dunno what that means"

def ansi_home():
	print "ok,you enter the home of the gadget freak"
	print "you wanna switch off his comp and get screwed or sit there and get bugged"
	next = raw_input()
	if next == 'switch off comp':
		print "you have taken a deadly decision,you mite get hit anytime"
	elif next== 'get bugged':
		print "gone are your happy days"
	else:
		print "type something related"
	
def synthia_home():
	print "you are entering the home of the bulldozer"
	print "you pull her out to play a game of shuttle or sit there and let your ears bleed"
	next = raw_input()
	if next == 'play':
		print"you can expect little tremors as she walks out "
	elif next =='sit there':
		print"why blood,same blood"
	else:
		print "oh! man are you mad"
		
land()
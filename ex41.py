from sys import exit
from random import randint

def death() :
	quips = ["you died. you kinda suck at this",
			 "nice job,you died.....jackass",
			 "such a loser",
			 "i have a small puppy that's better at this"]
		
	print quips[randint(0, len(quips)-1)]
	exit(1)
	
def central_corridor():
	print "the gothons of planet percal #25 have invaded your ship and destroyed"
	print "your entire crew.you are the last surviving member and your last"
	print "mission is to get the neutron destruct bomb from the weapons armory"
	print "put it in the bridge,and blow the ship up after getting into an"
	print "escape pod"
	print "\n"
	print "you're running down the central corridor to the weapons armory when"
	print "a gothon jumps out,red scaly skin,dark grimy teeth,and evil clown costume"
	print "flowing around his hate filled body.he is blocking the door to the"
	print "armory and about to pull a weapon to blast you"
	
	action = raw_input(">")
	
	if action == "shoot!":
		print "quic on the draw you yank out your blaster and fire it at the gothon :"
		print "his clown costume is flowing and moving around his body,which throws"
		print "off your aim.your laser hits his costume but misses him entirely"
		print "completely ruins his brand new costume his mother bought him,which"
		print "makes him fly into insane rage and blast you repeatedly int the fact "
		print "you are dead.Then he eats you"
		return 'death'
		
	elif action == "dodge!":
		print "like a world class boxer you dodge,weave,slip and slide right"
		print "as the gothon's blaster cranks a laser past your head"
		print "in the middle of your artful dodge your foot slips and you"
		print "bang your head on the metal wall and pass out"
		print "you wake up shortly after only to die as the gothon stomps on"
		print "your head and eats you"
		return 'death'
	
	elif action =="tell a joke":
		print "lucky for you they made you learn gothon insults in the academy"
		print "you tell the one gothon joke you know"
		print "lbhe zbgure vf fb sng,jura fur fvgv kjkj kjhkl uguhbjh"
		print "the gothon stops,tries not to laugh,then busts out laughing and can't move"
		print "while he is laughing you run up and shoot him square in the head"
		print "putting him down then jump through the weapon armory door"
		return 'laser_weapon_armory'
		
	else:
		print "does not compute"
		return 'central_corridor'
		
def laser_weapon_armory():
	print "you do a dive roll into the weapon armory,crouch and scan the room"
	print "for more gothons that might be hiding.it's a dead quiet,too quiet"
	print "you stand up and run to the far side of the room and find the"
	print "neutron bomb in its container there's a keypad lock on the box"
	print "and you need the code to get the bomb out if you get the code"
	print "wrong 10 times then the lock closes forever and you can't"
	print "get the bomb.the code is 3 digits"
	code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
	guess = raw_input("[keypad]>")
	guesses = 0
	
	while guess != code and guesses <10:
		print "BZZZZEDDD"
		guesses += 1
		guess = raw_input("[keypad]> ")
		
	if guess == code:
		print "the container clicks open and the seal breaks,letting gas out "
		print "you grab the neutron bomb and run as fast as you can to the "
		print "bridge where you must place it in the right spot"
		return 'the_bridge'
	else:
		print "the lock buzzes one last time and then you hear a sickening "
		print "melting sound as the mechanism is fused together "
		print "you decide to sit there an finlly the gothons blow up the"
		print "ship from their ship and you die"
		return 'death'
		
def the_bridge():
	print "you burst onto the bridge with the neutron destruct bomb"
	print "under your arm and surprise 5 gothons who are trying to"
	print "take control of the ship.each of them has an even uglier"
	print "clown costume than the last,they haven't"
	print "pulled their weapons out yet,as they see the active bomb under your"
	print "arm and don't want to set it off"
	
	action = raw_input("> ")
	
	if action == "throw the bomb":
		print "in a panic you throw the bomb at the group of gothons"
		print "and make a leap for the door.right as you drop it a "
		print "gothon shoots you right in the back killing you"
		print "as you die you see another gothon frantically try to disarm"
		print "the bomb.you die knowing they will probably blow up when"
		print "it goes off"
		return 'death'
		
	elif action == "slowly place the bomb":
		print "you point your blaster at the bomb under your arm"
		print "and the gothons put their hands up and start to sweat"
		print "you inch backward to the door open it an dthen carefully"
		print "place the bomb on the floor,pointing your blaster at it"
		print "you then jump back through the door punch the close button"
		print "and blast the lock so the gothon can't get out"
		print "now that the bomb is placed yoy run to the escape"
		print "get off this thin can"
		return 'escape_pod'
		
	else:
		print "does not compute"
		return "the_bridge"
		
def escape_pod():
	print "you rush through the ship desperately trying to make it to"
	print "the escape pod before the whole ship explodes.it seems like"
	print "hardly any gothons are on the ship,so your run is clear of"
	print "interference.you get to the chamber with the escape pods,and"
	print "now need to pick one to take.some of them could be damaged"
	print "but you don't have time to look.ther's 5 pods which one"
	print "do you take"
	
	good_pod = randint(1,5)
	guess = raw_input("[pod #]>")
	
	if int(guess) != good_pod:
		print "you jump into %s nd hit the eject button" % guess
		print "the pod escapes out into the void space,then"
		print "implodes as the hull ruptures,crushing your body"
		print "into into jam jelly"
		return 'death'
	else:
		print "you jump into pod %s and hit the eject button" % guess
		print "the pod easily slides out into the void space,then"
		print "the planet below.as it flies to the planet,you look"
		print "back and see your ship implode then explode like a"
		print "bright star,aking out the gothom ship at the same"
		print "time.you won"
		exit(0)
		
ROOMS = {
	'death':death,
	'central_corridor':central_corridor,
	'laser_weapon_armory' :laser_weapon_armory,
	'the_bridge':the_bridge,
	'esacpe_pod':escape_pod
}

def runner(map,start):
	next = start
	
	while True:
		room = map[next]
		print "\n-----------"
		next = room()
		
runner(ROOMS,'central_corridor')
		
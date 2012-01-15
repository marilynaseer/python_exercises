def hi(*args):
	arg1,arg2 = args
	print "arg1: %r,arg2: %r" % (arg1,arg2)
	
def hello(arg1,arg2):
	print "arg1: %r,arg2: %r" % (arg1,arg2)
	
def printo(arg1):
	print "arg1:%r"% arg1

def print1():
	print "none"

hi("merl","mer")
hello("merl","mer")
printo("erl")
print1()
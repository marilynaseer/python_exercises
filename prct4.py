from sys import argv
script,filename = argv

print "we are gonna delete %r"% filename
print "press ctrl+c if u don't wanna do it"
print "else press return"

target = open(filename,'w')
print "truncating"

target.truncate()

print "write into file"
line1 = raw_input("hello")
line2 = raw_input("good day")

target.write(line1)
target.write(line2)
target.close()
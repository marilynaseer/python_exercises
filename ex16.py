from sys import argv

script,filename =argv

print "we are going to erase %r"%filename
print "if you don't want that,hit ctrl+c"
print "if you do not want that, hit return"

raw_input("?")

print "opening the file.."
target=open(filename,'w')

print"trucating the file"
target.truncate()

print "enter three lines"

line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")

print "i am going to write three lines"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print"close"
target.close()
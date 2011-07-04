from sys import argv

script,filename=argv

txt=open(filename)


print"here is your file %r"%filename
print txt.read()

print "i will also ask you to type it gain:"
file_again=raw_input(">")

txt_again=open(file_again)

print txt_again.read()
txt.close()
txt_again.close()

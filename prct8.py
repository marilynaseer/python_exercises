def party_checklist(decoration,eatables):
	print "we need %r different items for decorating" % decoration
	print "we need %r different varieties of food" % eatables
	
party_checklist(20,50)

print"or we can do this"
no_of_decorations = 20
no_of_eatables = 50
party_checklist(no_of_decorations,no_of_eatables)

party_checklist(no_of_decorations + 20,no_of_eatables + 40)
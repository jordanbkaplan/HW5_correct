import re
fname=open("regex_sum_31499.txt", "r")
aq=0
for a in fname:
	#print (a)
	b=re.findall("[0-9]+",a)
	for a in b:
		#print (a)
		aq+=int(a)

print (aq)
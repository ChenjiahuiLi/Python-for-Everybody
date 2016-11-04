import re
hand = open("mbox-short.txt")

for line in hand:
	line = line.rstrip()
	#lst = re.findall('\S+@\S+',line)
	lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]',line)
	if len(lst)>0:
		print lst

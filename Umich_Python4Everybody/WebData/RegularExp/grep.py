import re

regname = raw_input("Enter a regular expression:")
if len(regname) < 1 : regname = '^From'

count = 0

hand = open("mbox-short.txt")
for line in hand:
	line = line.rstrip()
	if re.findall(regname, line):
		print line
		count += 1
		
print(count)

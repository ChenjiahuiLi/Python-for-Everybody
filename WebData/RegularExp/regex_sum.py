import re

fname = raw_input("Enter file name:")
if len(fname)<1 : fname = "regex_sum.txt"
fh = open(fname)
lst = list()
for line in fh:
	number = re.findall('[0-9]+', line)
	length = len(number)
	if length>0: 
		for i in number:
			lst.append(int(i))
# print lst
print sum(lst)


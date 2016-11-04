# Assignment 8.4
fname = raw_input("Enter file name: ")
if len(fname) < 1: fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    lst.extend(line)
lst.sort()

# print lst
l = len(lst) - 1
r = range(len(lst))
del r[l]
# print lst
count = 0
# print range(len(lst)-1)
t = list()
for i in range(len(lst)-1):
    if lst[i] == lst[i+1]:
        t.append(i+1)
    else: continue

i = len(t)-1
while i>=0:
    del lst[t[i]]
    i -= 1
print lst


# Assignment 8.5
fname = raw_input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print words[1]
    count += 1

print "There were", count, "lines in the file with From as the first word"


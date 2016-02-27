stuff = dict()
print stuff.get('candy',-1)

name = raw_input("Enter files:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

email = list()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    t = words[1]
    email.append(t)
print len(email), email

counts = dict()
for name in email:
    counts[name] = counts.get(name,0) + 1
for key in counts:
    if counts[key] == max(counts.values()):
        print key, counts[key]

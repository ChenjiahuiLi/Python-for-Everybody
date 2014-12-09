purse = dict()

purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print purse
print purse['candy']
purse['candy'] += 2
print purse

# list maintain ORDER, dictionary don't maintain ORDER

# Most Common Name?
ccc = dict()
# print ccc['csev'] => traceback
# is 'csev' a current key in dictionary ccc
print 'csev' in ccc

counts = dict()
names = ['csev','cwem','csev', "zqian",'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print counts

# The logic above is so common that there is a method called get() that does this for us
counts = dict()
names = ['csev','cwen','csev', "zqian",'cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print counts

counts = dict()
print 'Enter a line of text:'
line = raw_input('')

words = line.split() # split a line into a list of word, a list!
print 'Words:',words

print 'Counting...'
for word in words:
    counts[word] = counts.get(word,0) + 1
print 'Counts',counts

counts = dict(chuck=1, fred=42, jan=100)
for key in counts:
    print key, counts[key]
print list(counts)
print counts.values()
print counts.items()

for aaa.bbb in counts.items():
    print aaa.bbb


# 10.11 Exercise 2
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
word = list()
for line in handle:
    if line.startswith('From'):
        l = line.split()
        if len(l) > 3:
            word.append(l[5])
# print len(word), word
time = list()
for ti in word:
    t = ti.split(':')
    time.append(t[0])
# print len(time)
counts = dict()
for hour in time:
    if hour not in counts:
        counts[hour] = 1
    else:
        counts[hour] += 1
# print counts

lst = counts.items()
# print type(lst)
lst.sort()
for key, val in lst[:27]:
    print key, val

# Notes
t = ('a','b','c')
t1 = ('a',)
print type(t1)
t2 = ('a')
print type(t2)
t = tuple()
print t
t = tuple('lupins')
print t[0]
print t[1:3]
t = ('A',) + t[1:]
print t

# How to use 'sort'
txt = 'but soft what light in yonder window breaks'
words = txt.split()
print type(words), words
t = list()
for word in words:
    t.append((len(word), word))
print(t)
t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print res

# Tuple Assignment
m = ['have', 'fun']
x, y = m
(x, y) = m
addr = 'monty@python.org'
uname, domain = addr.split('@')
print uname, domain

# How to use 'items' in dictionary and tuple
d = {'a':10, 'b':1, 'c':22}
t = d.items() # t is a list of tuples
print t # the items are not in a particular order
t.sort()
print t
for key, val in t:
    print val, key

# How to sort items in dictionary
d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items():
    l.append((val, key))
print l
l.sort(reverse=True)
print l


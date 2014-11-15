# Q1
str1 = "Hello"
str2 = "there"
bob = str1 + str2
print bob
# Hellothere  choose A

# Q2
x = '40'
y = int(x) + 2
print y
# 42

# Q3
x = 'From marquard@uct.ac.za'
index = x.find('q')
print index  # 8
print x[8]

# Q4
atpos = x.find('@')
sppos = x.find('.',atpos)
# print atpos :13
# print sppos :17
host = x[atpos+1:sppos]
print host

# Q5
# iteration variable is 'letter'

# Q6
print len('banana')*7

# Q7
greet = 'Hello Bob'
print greet.upper()

# Q8
print greet.lstrip('b')
print greet.join('b')

# Q9
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print data[pos:pos+3]
# .ma
# not .mar, even though pos+3
# 3 means the length of the string

# Q10
line = " Hello World "
line.strip()


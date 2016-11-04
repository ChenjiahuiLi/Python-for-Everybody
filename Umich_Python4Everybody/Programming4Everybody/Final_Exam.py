# Question 1
a = "123"
b = 456
#c = a+b  # causes a traceback: cannot concatenate 'str' and 'int' objects
#print c

# Question 2
# exponent: 2**(0.5)
q2 = 2**3*7+1 # Expondent > Multiplication > Addition
print q2

# Question 4
x = raw_input("Enter a number: ")
x = float(x)
if x < 2:
    print "Below 2"
elif x < 0:
    print "Negative"
else:
    print "Something else"

# Question 5
abc = "With three words"
stuff = abc.split()
print stuff

# Question 6
str = "hello there bob"
print str[4] # it's 'o', not 'l'

# Question 7
abc = 1 + 2 - 3 * 4 + 5 - 6 / 3
print abc

# Question 9
def fred():
   print "Zap"

def jane():
   print "ABC"

jane()
fred()
jane()

# Question 11
st = "abc"
ix  = int(st) # error

# Question 12
lst = []
lst.append(4)
lst.append(10)
lst.append(21)
lst.append(6)
print lst[2]
print lst # [4, 10, 21, 6]

# Question 15
sta = "abc"
stb = "123"
stc = sta + stb
print stc # abc123

# Question 16
x = 0
for value in [3, 41, 12, 9, 74, 15] :
    if value < 10 :
        x = x + value
print x

# Question 17
fline = "blah blah"

if len(fline) > 1 :
    print "More than one"
    if fline[0] == "h" :
        print "Has an h"
print "All done"

# Question 18
abc = 1 - 2 + 3 * 4 - 5 - 6 / 3
print abc

# Question 19
stx = "hello there bob how are you"
wds = stx.split()
print wds[2] # bob



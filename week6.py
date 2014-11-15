fruit = "banana"
letter = fruit[1]
print letter
letter = fruit[0]
print letter

len(fruit)
length = len(fruit)
last = fruit[length - 1]
print length
print last
print fruit[-2]

# Traversal
# while
index = 0
while index < length:
    letter = fruit[index]
    print letter
    index = index + 1

index = length - 1
while index > -1:
    letter = fruit[index]
    print letter
    index = index - 1
# for
for char in fruit:
    print char

# Slice: a segment of a string
s = "Monty Python"
print len(s)
print s[0:5]
print s[6:12]
text = "X-DSPAM-Confidence:    0.8475"
text1 = "X-DSPAM-Confidence:"
print len(text)
print len(text1)
print text[23:29]
value = text[23:29]
v = float(value)
print v

print fruit[:]  # banana

# Change the string
greeting = "Hello World"
new_greeting = "J" + greeting[1:]
print new_greeting

# Looping & Counting
word = "banana"
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print count


def count(word, l):
    c = 0
    for letter in word:
        if letter == l:
            c += 1
    return c


coun = count("banana", 'a')
print coun

# in ?
var = 'a' in "banana"

# dir & type
stuff = "Hello World"
type(stuff)
dir(stuff)  # docs.python.org/library/string.html
new_stuff = stuff.upper()
print new_stuff
# eg: find()
text = "X-DSPAM-Confidence:    0.8475"
index = text.find('0.8475')
print type(index)
t = text[index:]
print type(t)
t = float(t)
print t
# eg: remove white spaces
line = " Hello World "
line.strip()
line = "Please have a nice day"
line.startswith('Please')
line.lower().startswith('p')









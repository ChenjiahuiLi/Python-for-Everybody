# Collection: a variable with multiple values
friends = ["J", "G", "K"]
print friends[1]
# we can change single item in list, but not in string, because a string is one element
print range(4)
# [0,1,2,3]
print len(friends) # 3
print(range(len(friends)))
# if we need to change something about the loop, better give an i !
for i in range(len(friends)):
    friend = friends[i]
    print "Happy New Year:", friend

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print c
print len(c)

t = [9, 41, 12, 3, 74, 15]
print t[2:4]

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print friends[0]
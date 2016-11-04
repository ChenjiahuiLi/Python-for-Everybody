# Assignment 1
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    t = line.upper()
    print t

# Assignment 2
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
summ = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence: "):
        count += 1
        text1 = line
        value = text1[-7:-1]
        summ = summ + float(value)
    else:
        continue

mean = summ/count

print 'Average spam confidence:', mean

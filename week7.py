# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    #t = line.rstrip()
    t = line.upper()
    print t


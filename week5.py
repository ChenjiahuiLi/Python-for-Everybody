__author__ = 'submarine'

largest = 7
smallest = 4
while True:
    num = raw_input("Enter a number: ")

    # Handle the edge cases
    if num == "done" : break

    try:
        h = float(num)
    except:
        print("Invalid input")
        continue

    print num

print "Maximum is", largest
print "Minimum is", smallest
def computepay(h,r):
    if h>40.00:
        pay = 40.00*r+(h-40.00)*1.5*r
    else:
        pay = h*r
    return pay

hrs = raw_input("Enter Hours:")
h = float(hrs)
r = float(10.50)
p = computepay(h, r)
print p
def mergeSort(alist,ns):
    #print("Splitting ",alist)

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        lefthalf,n1 = mergeSort(lefthalf,ns)
        righthalf,n2 = mergeSort(righthalf,ns)
        #print(n1,n2)
        ns = n1+n2
        #print(ns)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
                ns = ns + len(lefthalf) - i   # this update is the key !!!!
                #print ns
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    #print("Merging ",alist)
    #print ns
    return alist, ns


# Execution on the 10,000,000 array
f = open('IntegerArray.txt','r')
lines = f.readlines()
alist = [int(i) for i in lines]
ns = 0

a,n = mergeSort(alist,ns)
print(a,n)

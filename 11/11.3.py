import math
import random

def almost_sorted_ints_reversed(n):
    l = list(range(0, n))
    l.reverse()
    for i in range(0, int(math.sqrt(n))):
        index = random.randint(0, n-2);
        tmp = l[index]
        l[index] = l[index+1]
        l[index+1] = tmp
    return l

def cmp(a, b):
    return (a > b) - (a < b) 

def swap(L, i, k):
    tmp = L[i]
    L[i] = L[k]
    L[k] = tmp

def selectsort(L, left, right, cmpfunc=cmp):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if cmpfunc(L[j], L[k]) < 0:
                k = j
        swap(L, i, k)


#zastosowanie
reversedlist = almost_sorted_ints_reversed(50)
print(reversedlist)
selectsort(reversedlist, 0, 49, cmp)
print(reversedlist)

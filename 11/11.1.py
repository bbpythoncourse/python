import random
import math

def rand_ints(n):
    return random.shuffle(range(0, n))

def almost_sorted_ints(n):
    l = [range(0, n)]
    tmp = l[0]
    l[0] = l[n-1]
    l[n-1] = tmp
    return l

def almost_sorted_ints_reversed(n):
    l = [range(0, n)].reverse()
    tmp = l[0]
    l[0] = l[n-1]
    l[n-1] = tmp
    return l

def gaussian_floats(n):
    l = []
    for i in range(n):
        l.append(random.uniform(0, 10))
    return l

def repeating_ints(n):
    l = []
    for i in range(n):
        l.append(random.randint(0, math.sqrt(n)))
    return l
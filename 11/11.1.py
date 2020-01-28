import random
import math

def rand_ints(n):
    l = [range(0, n)]
    random.shuffle(l)
    return l

def almost_sorted_ints(n):
    l = [range(0, n)]
    for i in range(0, int(math.sqrt(n))):
        index = random.randint(0, n-2);
        tmp = l[index]
        l[index] = l[index+1]
        l[index+1] = tmp
    return l

def almost_sorted_ints_reversed(n):
    l = [range(0, n)].reverse()
    for i in range(0, int(math.sqrt(n))):
        index = random.randint(0, n-2);
        tmp = l[index]
        l[index] = l[index+1]
        l[index+1] = tmp
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
from random import randint

def randomList(n, k):
    L = []
    for i in range(0, n):
        L.append(randint(0, k - 1))
    return L

def linearSearch(L, y):
    result = []
    for i, number in enumerate(L): 
        if number == y:
            result.append(i)
    return result

n = 100
k = 10
L = randomList(n, k)
result = linearSearch(L, randint(0, k - 1))
print(result)


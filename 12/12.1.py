from random import randint

def randomList(n, k):
    L = []
    for i in range(0, n):
        L.append(randint(0, k - 1))
    return L

def linearSearch(L, y):
    for number in L: 
        if number == y:
            print(number)

n = 100
k = 10
L = randomList(n, k)
linearSearch(L, randint(0, k - 1))



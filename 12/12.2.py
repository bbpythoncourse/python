from random import randint

def randomList(n, k):
    L = []
    for i in range(0, n):
        L.append(randint(0, k - 1))
    return L

def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if left > right:
        return
    k = int((left+right) / 2)
    if y == L[k]:
        return k
    if y > L[k]:
        return binarne_rek(L, k+1, right, y)
    else:
        return binarne_rek(L, left, k-1, y)

n = 100
k = 10
L = randomList(n, k)
L.sort()
print(binarne_rek(L, 0, n - 1, 5))


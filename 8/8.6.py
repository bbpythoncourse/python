import timeit

memory = dict()

def recursive(i, j):
    if i == 0 and j == 0:
        return 0.5
    if i > 0 and j == 0:
        return 0
    if i == 0 and j > 0:
        return 1
    return 0.5 * (recursive(i-1, j) + recursive(i, j-1))

def dynamic(i, j):
    if i == 0 and j == 0:
        return 0.5
    if i > 0 and j == 0:
        return 0
    if i == 0 and j > 0:
        return 1
    if (i, j) in memory:
        return memory[(i, j)]
    memory[(i, j)] = 0.5 * (dynamic(i-1, j) + dynamic(i, j-1))
    return memory[(i, j)]

print("dynamicznie: " + str(dynamic(11, 15)))
print("rekursywnie: " + str(recursive(11, 15)))

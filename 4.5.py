def odwracanie(L, left, right):
    if(left == right or left > right):
        return

    tmp = L[left]
    L[left] = L[right]
    L[right] = tmp

    odwracanie(L, left + 1, right - 1)


def odwracanie_iteracyjnie(L, left, right):
    if(left == right or left > right):
        return

    mid = (left + right) // 2
    for index, i in enumerate(range(left, mid + 1)):
        print("i:" + str(i))
        print("right - i:" + str(right - i))
        tmp = L[i]
        L[i] = L[right - index]
        L[right - index] = tmp


L = [2, 4, 5, 7, 8, 9, 10]
copy = list(L)

odwracanie_iteracyjnie(L, 1, 5)

print(L)

odwracanie(L, 1, 5)

print(L)

assert(L == copy)

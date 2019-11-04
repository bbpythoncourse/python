def fibonacci(n):
    if n == 1 or n == 2:
        return 1
        
    prev, curr = 1, 1

    for i in range(2, n):
        tmp = prev
        prev = curr
        curr = prev + tmp

    return curr

x = int(input())
print(fibonacci(x))

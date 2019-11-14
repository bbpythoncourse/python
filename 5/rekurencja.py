def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    prev, curr = 1, 1

    for i in range(2, n):
        tmp = prev
        prev = curr
        curr = prev + tmp

    return curr

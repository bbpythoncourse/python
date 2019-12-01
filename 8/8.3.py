import random

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo. n oznacza liczbę losowanych punktów."""
    circle_count = 0
    square_count = 100

    for i in range(100):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x*x + y*y < 1:
            circle_count += 1

    return 4 * circle_count / square_count

print(calc_pi(100))

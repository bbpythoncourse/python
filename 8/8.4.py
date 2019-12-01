from math import sqrt

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("niespelniony warunek trojkata")
    return sqrt((a + b + c)*(a + b - c)*(a - b + c)*(-a + b + c) / 4)

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

print(heron(a, b, c))
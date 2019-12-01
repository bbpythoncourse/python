def solve1(a, b, c): 
    return "x = " + str(-b/a) + "y + " + str(-c/a)

print("Prosze podać parametry:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print("Rozwiazanie: " + solve1(a, b, c))
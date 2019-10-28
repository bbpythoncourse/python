x = [1, 3, 4]
y = (1, "a", 4)


s = set(x)
both = s.intersection(y)
all = s.union(y)

print("lista wszystkich elementow wystepujacych jednoczesnie w obu sekwencjach (bez powtorzen): " + str(list(both)))
print("lista wszystkich elementow (bez powtorzen): " + str(list(all)))

x = int(input())
result = "|"
numbers = "0"

for i in range(x):
    result += "....|"
    numbers += str(i + 1).rjust(5)

result += "\n" + numbers

print(result)
    
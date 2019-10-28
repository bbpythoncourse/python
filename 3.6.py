height = int(input("heigth = "))
width = int(input("width = "))

result = ""

for j in range(height):
    result += "+"
    for i in range(width):
        result += "---+"
    result += "\n|"
    for i in range(width):
        result += "   |"
    result += "\n"

result += "+"
for i in range(width):
    result += "---+"



print(result)
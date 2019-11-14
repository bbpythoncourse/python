def miarka(input):
    result = "|"
    numbers = "0"

    for i in range(input):
        result += "....|"
        numbers += str(i + 1).rjust(5)

    result += "\n" + numbers
    return result


def kratka(height, width):
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

    return result


x = int(input("x="))
result = miarka(x)
print(result)

height = int(input("heigth = "))
width = int(input("width = "))

result = kratka(height, width)
print(result)

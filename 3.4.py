x = ""
while x != "stop":
    try:
        x = input()
        if x == "stop":
            break
        print(x + " " + str(float(x)**3))
    except ValueError:
        print("blad, wpisz liczbe")

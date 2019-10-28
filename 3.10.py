def roman_to_int(input):
    signs = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0
    for i in range(len(input)):
        val = signs[input[i]]
        if i+1 < len(input) and signs[input[i+1]] > val:
            sum -= val
        else:
            sum += val
    return sum


print(roman_to_int("VL"))

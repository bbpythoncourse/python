def sum_seq(sequence):
    total = 0

    for element in sequence:
        if isinstance(element, (list, tuple)):
            total += sum_seq(element)
        else: 
            total += element

    return total

L = [(1, 2), 3, [4, 5]]
    
print(sum_seq(L))
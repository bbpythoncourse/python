
def flatten(seq):
    result = []
    
    for element in seq:
        if isinstance(element, (list, tuple)):
            result += flatten(element)
        else: 
            result.append(element)

    return result


seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))            # [1,2,3,4,5,6,7,8,9]
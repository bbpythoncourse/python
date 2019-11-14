def sort_by_len(lines):
    splitted = lines.split()
    splitted.sort(key=len)
    return splitted

lines = """napis wielowierszowy 
        \t    jeszcze pare
         wyrazow"""
        
print(sort_by_len(lines)[-1])
print(len(sort_by_len(lines)[-1]))

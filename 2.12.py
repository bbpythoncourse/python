def split_lines(line):
    splitted = line.split('\n')
    return [x.strip() for x in splitted]

def get_characters_from_index(index):
    return ''.join([x[index] for x in lines])

line = """napis wielowierszowy 
        \t    jeszcze pare
         wyrazow"""

lines = split_lines(line)
print(get_characters_from_index(0))
print(get_characters_from_index(-1))
line = """napis wielowierszowy 
        \t    jeszcze pare
         wyrazow"""

print(sum([len(word) for word in line.split()]))
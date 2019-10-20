lines = """napis wielowierszowy GvR
        \t    jeszcze pare
  GvR       wyrazow"""

splitted = lines.split()
sorted_alphabetic = sorted(splitted)
sorted_by_len = sorted(splitted, key=len)
print(sorted_alphabetic)
print(sorted_by_len)
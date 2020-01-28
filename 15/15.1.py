def mul_perm(perm1, perm2):         # perm1*perm2
    L = []
    for item in perm2:
        L.append(perm1[item])
    return L

def invert_perm(perm):             # permutacja odwrotna
def is_identity(perm):              # bool, czy identyczność
    for i, num in enumerate(jeden):
        if num != i:
            return False
    return True

def find_order(perm): pass              # rząd (krotność) permutacji

jeden = range(N)                        # identyczność
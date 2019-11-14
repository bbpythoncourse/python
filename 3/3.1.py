#prawidłowa skladnia, ale sredniki nie sa wymagane
x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;

## niepoprawna składnia, najpierw print i a potem if powinien byc
for i in "qwerty": if ord(i) < 100: print i

# poprawna skladnia
for i in "axby": print ord(i) if ord(i) < 100 else i
# Problem drogi skoczka na kwadratowej szachownicy o boku N.
# Współrzędne planszy x i y mają zakres od 0 do N-1.

def rysuj():
    for i in range(N):
        for j in range(N):
            print("%2s" % plansza[i, j])
        print

def dopuszczalny(x, y):
    return 0 <= x < N and 0 <= y < N and plansza[x, y] == 0

def zapisz(krok, x, y):
    plansza[x, y] = krok   # zapis ruchu

def wymaz(x, y):
    plansza[x, y] = 0

def probuj(krok, x, y):
    # krok - nr kolejnego kroku do zrobienia
    # x, y - pozycja startowa skoczka
    # Funkcja zwraca bool True/False (czy udany ruch).
    udany = False
    kandydat = 0          # numery od 0 do RUCHY_SKOCZKA-1
    while (not udany) and (kandydat < RUCHY_SKOCZKA):
        u = x + delta_x[kandydat]         # wybieramy kandydata 
        v = y + delta_y[kandydat]
        if dopuszczalny(u, v):
            zapisz(krok, u, v)
            if krok < N * N:         # warunek końca rekurencji
                udany = probuj(krok+1, u, v)
                if not udany:
                    wymaz(u, v)
            else:
                udany = True
        kandydat += 1
    return udany

N = 6  # bok szachownicy
RUCHY_SKOCZKA = 8

# Inicjalizacja pustej planszy.
plansza = {}
for i in range(N):
    for j in range(N):
        plansza[i, j] = 0

# . 2 . 1 .   kolejne możliwe ruchy skoczka
# 3 . . . 0
# . . x . .
# 4 . . . 7
# . 5 . 6 .

delta_x = [2,1,-1,-2,-2,-1,1,2]         # różnica współrzędnej x
delta_y = [1,2,2,1,-1,-2,-2,-1]         # różnica współrzędnej y
(x0, y0) = (2, 2)                       # pole startowe skoczka

zapisz(1, x0, y0)

if probuj(2, x0, y0):
    print("Mamy rozwiązanie")
    rysuj()
else:
    print("Nie istnieje rozwiązanie")
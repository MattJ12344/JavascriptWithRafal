import math

def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def znajdz_liczby_pierwsze_suma(n):
    for i in range(3, n // 2 + 1, 2):
        if czy_pierwsza(i) and czy_pierwsza(n - i):
            return i, n - i

with open("Pary.txt", "r", encoding='utf-8') as f:
    for line in f:
        liczby = line.split()
        liczba = int(liczby[0])
        
        if liczba % 2 == 0 and liczba > 4:
            pierwsza1, pierwsza2 = znajdz_liczby_pierwsze_suma(liczba)
            
            print(f";{liczba};{min(pierwsza1, pierwsza2)};{max(pierwsza1, pierwsza2)}")
        
        

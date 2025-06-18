import math

def czy_pierwsza(n):
    if n < 2:
        return False
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True

with open('liczbypierwsze.txt', 'r') as file:
    zawartosc = file.read()


lis = [int(x) for x in zawartosc.split()]

for liczba in lis:
    if czy_pierwsza(liczba):
        print("TAK;")
    else:
        print("NIE;")
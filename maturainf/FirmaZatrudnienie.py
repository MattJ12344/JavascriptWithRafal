wynik = 0
aktualna_pensja_wszystkich = 0
pracownicy = {}
with open("zapis.txt", "r", encoding='utf-8') as f:
    for line in f:
        podzielone = line.split()
        if podzielone[0] == "zwalniam":
            wynik += aktualna_pensja_wszystkich
            aktualna_pensja_wszystkich -= pracownicy[podzielone[1]]
            pracownicy.pop(podzielone[1])
        else:
            aktualna_pensja_wszystkich += int(podzielone[2])
            pracownicy[podzielone[1]] = int(podzielone[2])
            wynik += aktualna_pensja_wszystkich

print (wynik)
with open('liczby.txt', 'r') as plik:
    wiersze = plik.readlines()
    
liczby_pierwsze_string = wiersze[0].strip().split(' ')
liczby_calkowite_string = wiersze[1].strip().split(' ')
liczby_pierwsze = []
liczby_calkowite = []

for liczba_pierwsza in liczby_pierwsze_string:
    liczby_pierwsze.append(int(liczba_pierwsza))
for liczba_calkowita in  liczby_calkowite_string:
    liczby_calkowite.append(int(liczba_calkowita))
    
ile_liczb_z_dzielnikiem = 0
for liczba_pierwsza in liczby_pierwsze:
    for liczba_calkowita in liczby_calkowite:
        if liczba_calkowita % liczba_pierwsza == 0:
            ile_liczb_z_dzielnikiem +=1
            break
        


print(f'Zadanie 4.1: {ile_liczb_z_dzielnikiem}')

#Zadanie 4.2
posortowane_pierwsze = sorted(liczby_pierwsze, reverse=True)
print(f'Zadanie 4.2: {posortowane_pierwsze[100]}')
#Zadanie 4.3
def rozklad_na_czynniki(n):
    czynniki = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            czynniki.append(i)
            n = n // i
        i = i + 1 
    if n > 1:
        czynniki.append(n)
    return czynniki

print('Zdanie 4.3 :')
for liczba_calkowita in liczby_calkowite:
    czynniki = rozklad_na_czynniki(liczba_calkowita)
    liczby_pierwsze_kopia = liczby_pierwsze.copy()
    czy_sie_uda = True
    for czynnik in czynniki:
        if czynnik not in liczby_pierwsze_kopia:
            czy_sie_uda = False
            break
        else:
            liczby_pierwsze_kopia.remove(czynnik)
    if czy_sie_uda:
        print(liczba_calkowita)
        

# Zadanie 4.4
najwyzsza_srednia = 0
najwyzsza_liczba_elementow = 50
najwyzsza_pocztek = -1

for rozmiar_okna in range(50, len(liczby_pierwsze) + 1):
    suma = sum(liczby_pierwsze[:rozmiar_okna])
    aktualna_srednia = suma / rozmiar_okna
    if aktualna_srednia > najwyzsza_srednia:
        najwyzsza_srednia = aktualna_srednia
        najwyzsza_pocztek = 0
        najwyzsza_liczba_elementow = rozmiar_okna
    
    for i in range(rozmiar_okna, len(liczby_pierwsze)):
        suma = suma + liczby_pierwsze[i] - liczby_pierwsze[i - rozmiar_okna]
        aktualna_srednia = suma / rozmiar_okna
        if aktualna_srednia > najwyzsza_srednia:
            najwyzsza_srednia = aktualna_srednia
            najwyzsza_pocztek = i - rozmiar_okna + 1
            najwyzsza_liczba_elementow = rozmiar_okna


print(f'Max średnia: {najwyzsza_srednia}')
print(f'najwyzsza_liczba_elementow: {najwyzsza_liczba_elementow}') 
print(f'najwyzsza_pocztek: {liczby_pierwsze[najwyzsza_pocztek]}')
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


posortowane_pierwsze = sorted(liczby_pierwsze, reverse=True)
print(f'Zadanie 4.2: {posortowane_pierwsze[100]}')
#Zadanie 4.2
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
#Zadanie 4.3
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
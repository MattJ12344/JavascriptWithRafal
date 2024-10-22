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



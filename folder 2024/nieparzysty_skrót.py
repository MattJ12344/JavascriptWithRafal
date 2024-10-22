with open('skrot.txt', 'r') as plik:
        wiersze = plik.readlines()

liczba_bez_skrotu = 0
max_liczba_bez_skrotu = -1

    
for wiersz in wiersze:
    skrot = wiersz.strip()
    czy_moze_miec_skrot = False
    for cyfra in skrot:
        cyfra = int(cyfra)
        if cyfra % 2 == 1:
            czy_moze_miec_skrot = True
                
    if not czy_moze_miec_skrot:
        liczba_bez_skrotu +=1
        skrot = int(skrot)
        if skrot > max_liczba_bez_skrotu:
            max_liczba_bez_skrotu = skrot



print(liczba_bez_skrotu)
print(max_liczba_bez_skrotu)
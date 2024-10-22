import math
def nieparzysty_skrot(n):
    potega = 1
    m = 0
    while n > 0:
        cyfra = n % 10
        if cyfra % 2 == 1:  
            m += potega * cyfra
            potega *= 10
        n //= 10
        
    return m

with open('skrot2.txt', 'r') as plik:
        wiersze = plik.readlines()
        
for wiersz in wiersze:
    liczba  = int(wiersz)
    liczba_skrot = nieparzysty_skrot(liczba)
    
    if math.gcd(liczba, liczba_skrot) == 7:
        print(liczba) 
    

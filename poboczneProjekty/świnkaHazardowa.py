import random

def losowanieSwinka() -> int:
    minimalnaWartosc:int = 1
    maksymalnaWartosc:int  = 6
    
    losuj = random.randint(minimalnaWartosc, maksymalnaWartosc)
    
    return losuj

while True:
    gracze:str = input("Ile ma zagrac graczy (2-4): ")
    
    if gracze.isdigit():
        gracze = int(gracze)
        if 2 <= gracze <= 4:
            break
        
        else:
            print("Musi być pomiędzy 2 lub do 4 graczy.")
            


maksimumPunktow: int = 50
punktyGracza = [0 for _ in range(gracze)]

while max(punktyGracza) < maksimumPunktow:
    for indexGracza in range(gracze):
        print("\n Gracz numer", indexGracza + 1, "ture rozpoczal")
        print("Twoj wynik calkowity wynosi:", punktyGracza[indexGracza], "\n")
        bierzacypunkt = 0
        
        while True:
            czyLosowac:str = input("Czy chcesz losowac (y)? ")
            
            if czyLosowac.lower() != "y":
                break
            
            wartosc:int = losowanieSwinka()
            
            if wartosc == 1:
                print("Wylosowales 1! Koniec tury!")
                bierzacypunkt:int = 0
                break
            
            else:
                bierzacypunkt += wartosc
                print("Wylosowales:", wartosc)
                
            print("Twoj wynik:", bierzacypunkt)
            
        punktyGracza[indexGracza] += bierzacypunkt
        print("Twoj wynik calkowity wynosi:", punktyGracza[indexGracza])


maksimumPunktow = max(punktyGracza)
wygrany = punktyGracza.index(maksimumPunktow)
print("Numer Gracza", wygrany + 1, "jest zwyciesca z wynikiem: ", maksimumPunktow )
            
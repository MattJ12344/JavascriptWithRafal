import random
from words import wordList

def pobierzSlowo():
    slowo = random.choice(wordList)
    return slowo.upper()

def zabawaWisielca(slowo):
    uzupelnianieSlowa = "_" * len(slowo)
    
    zgadywanie = False
    
    odgadnieteLitery = []
    
    odgadnieteSlowa = []
    
    proby = 6
    
    print("Zagrajmy w Wisielca")
    
    print(rozrywkaWisielca(proby))
    
    print(uzupelnianieSlowa)
    
    print("\n")
    
    
    while not zgadywanie and proby > 0:
        odgadywac = input("Prosze zgadnac literke lub slowo: ").upper()
        
        if len(odgadywac) == 1 and odgadywac.isalpha():
            if odgadywac in odgadnieteLitery:
                print("Już zgadles litere", odgadywac)
                
            elif odgadywac not in slowo:
                print(odgadywac, "nie jest w slowie.")
                proby -= 1
                odgadnieteLitery.append(odgadywac)
                
            else:
                print("Dobra robota,", odgadywac, "jest w slowie!")
                odgadnieteLitery.append(zgadywanie)
                slowoJakoLista = list(uzupelnianieSlowa)
                indeksy = [i for i, literka in enumerate(slowo) if literka == zgadywanie ] 
                
                for index in indeksy:
                    slowoJakoLista[index] = zgadywanie
                
                uzupelnianieSlowa = "".join(slowoJakoLista)
                
                if "_" not in  uzupelnianieSlowa:
                    zgadywanie = True
        
        
        elif len(odgadywac) == len(slowo) and odgadywac.isalpha():
            if zgadywanie in odgadnieteSlowa:
                print("Juz zgadles to slowo", zgadywanie)
            
            elif zgadywanie != slowo:
                print(zgadywanie, "nie jest slowem.")
                proby -= 1
                odgadnieteSlowa.append(zgadywanie) 
                
            else:
                zgadywanie = True
                uzupelnianieSlowa = slowo
            
        
        else:
            print("To nie jest trafne zgadywanie.")
            
        print(rozrywkaWisielca(proby))
        
        print(uzupelnianieSlowa)
        
        print("\n")
        
    if zgadywanie:
        print("Grarulacje, zgadles slowo! Wygrales gre!")
        
    else:
        print("Przepraszam skoczyly sie proby. Slow bylo takie " + slowo + ". Może nastepnym razem! ")
        
        
def rozrywkaWisielca(proby):
    czescWisielca =[
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """

                
    ]
    
    return czescWisielca[proby]


def main():
    slowo = pobierzSlowo()
    zabawaWisielca(slowo)
    
    while input("Chcesz jeszcze raz zagrac? (T/N) ").upper() == "T":
        slowo = pobierzSlowo()
        zabawaWisielca(slowo)
        

if __name__ == "__main__":
    main()
    
    
    
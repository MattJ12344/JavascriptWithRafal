import random
from typing import List

class Snake:
    
    # Konstruktor
    def  __init__(self, ruchyDoWykonania: List[str]) -> None:
        self.rozmiar: int = 3
        self.plansza: List[List[str]] = []
        self.snake: List[List[int]] = []
        self.owoce: List[List[int]] = []
        self.punkty: int = 0
        self.ruchy: List[str] = ruchyDoWykonania
    
        self.ileZjedzonychOwockow()
    
    def wygenerujPlansze(self) -> None:
        self.plansza = []
        
        for _ in range(self.rozmiar):
            wiersz: List[str] = []
            
            for _ in range(self.rozmiar):
                wiersz.append(' ')
                
            self.plansza.append(wiersz)

    def wygenerujSnake(self, x:int, y: int) -> None:
  
        self.snake = [[x, y]]
        self.plansza[x][y] = 'X'
        
    def postawOwoc(self, x:int, y:int) -> None:

        self.owoce.append([x, y])
        self.plansza[x][y] = 'O'
    
    def ileZjedzonychOwockow(self) -> int:
        return self.punkty
        
    def dodajPunkty(self) -> None:
        self.punkty += 1
        
    def wykonajRuchy(self) -> None:
        
        for kierunek in self.ruchy:
            
            if kierunek == 'w' or kierunek == 'W':
                x = -1 
                y = 0
                
            elif kierunek == 's' or kierunek == 'S':
                x = 1 
                y = 0
                
            elif kierunek == 'a' or kierunek == 'A':
                x = 0 
                y = -1
            
            elif kierunek == 'd' or kierunek == 'D':
                x = 0 
                y = 1
                
            else:
                continue
            
            wierszDoUsuniecia = 0
            iDoUsuniecia = 0
            
            for wiersz in range(len(self.plansza)):
                for i in range(len(self.plansza[wiersz])):
                    if self.plansza[wiersz][i] == 'X':
                        wierszDoUsuniecia = wiersz
                        iDoUsuniecia = i
                        
                        
            self.plansza[wierszDoUsuniecia][iDoUsuniecia] = ' '
            
            nowyX = wierszDoUsuniecia + x
            nowyY = iDoUsuniecia + y
            
            if not(0 <= nowyX < self.rozmiar and 0<= nowyY < self.rozmiar):
                continue
            
            if [nowyX, nowyY] in self.owoce:
                self.dodajPunkty()
                self.owoce.remove([nowyX, nowyY])
            
            self.snake[0] = [nowyX, nowyY]
            self.plansza[nowyX][nowyY] = 'X'
             
                    
                    
                    
                    
            # self.snake = [[x, y]]
            # self.plansza[x][y] = 'X'
            
           
            # 1. usuń weża/X z planszy
            #a) znalezc kordynaty dla 'X'
            #b) usunąć 'X' za pomocą znalezionych kordynatów (pop)
            # 2. wylicz kordynaty, gdzie ma być wąż
            # 3. ustaw węża według kordynatorów
            
            
            #1.
            # [X][][O]
            # [][][]
            # [][][]
            
            #2.
            # [][][O]
            # [][][]
            # [][][]
            
            #3.
            # [][X][O]
            # [][][]
            # [][][]
            
    
     
            
    def planszaNaString(self) -> str:
        wynik = ""
        
        for wiersz in self.plansza:
            for pole in wiersz:
                
                if pole == ' ':
                    wynik = wynik + "[]"
                    
                else:
                    wynik = wynik + "[" + pole + "]"
                    
            wynik = wynik + "\n"
            
        return wynik
            



#---Test1---
ruchyDoWykonania: List[str] = ["d", "d"]
waz1: Snake = Snake(ruchyDoWykonania)
waz1.wygenerujPlansze()
waz1.wygenerujSnake(0, 0)
waz1.postawOwoc(0, 2)

poczatkowaPlansza1: str = (
    "[X][][O]\n"
    "[][][]\n"
    "[][][]\n"
)

# print(waz1.planszaNaString())
# print(poczatkowaPlansza1)

assert waz1.planszaNaString() == poczatkowaPlansza1

waz1.wykonajRuchy()

spodziewanaPlansza1: str = (
    "[][][X]\n"
    "[][][]\n"
    "[][][]\n"
)

print(waz1.planszaNaString())
print(spodziewanaPlansza1)

assert waz1.planszaNaString() == spodziewanaPlansza1 , "Planasza zgadza się z spodziewaną"
assert waz1.ileZjedzonychOwockow() == 1

#nowa gra
#---Test2---

ruchyDoWykonania2: List[str] = ["s", "s", "d"]
waz2: Snake = Snake(ruchyDoWykonania2)
waz2.wygenerujPlansze()
waz2.wygenerujSnake(0, 0)
waz2.postawOwoc(2, 0)
waz2.postawOwoc(2, 1)



poczatkowaPlansza2: str = (
    "[X][][]\n"
    "[][][]\n"
    "[O][O][]\n"
)

assert waz2.planszaNaString() == poczatkowaPlansza2

waz2.wykonajRuchy()

spodziewanaPlansza2: str = (
    "[][][]\n"
    "[][][]\n"
    "[][X][]\n"
)


print(waz2.planszaNaString())
print(spodziewanaPlansza2)

assert waz2.planszaNaString() == spodziewanaPlansza2 , "Planasza zgadza się z spodziewaną"
assert waz2.ileZjedzonychOwockow() == 2

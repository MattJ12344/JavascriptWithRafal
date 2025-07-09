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
        self.koniecGry: bool = False
    
        
    
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
            
            
            glowaX, glowaY = self.snake[0]
            
            nowyX = glowaX + x
            nowyY = glowaY + y
            
            if not(0 <= nowyX < self.rozmiar and 0<= nowyY < self.rozmiar):
                self.koniecGry = True
                self.oznaczZakonczonaGre()
                return
            
            if [nowyX, nowyY] in self.snake:
                self.koniecGry = True
                self.oznaczZakonczonaGre()
                return
            
            self.snake.insert(0, [nowyX, nowyY])
            
            if [nowyX, nowyY] in self.owoce:
                self.owoce.remove([nowyX, nowyY])
                self.dodajPunkty()
            
            else:
                self.snake.pop()
                
            self.odswiezPlansze()
             
                    
                    
                    
                    
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
    
    def oznaczZakonczonaGre(self) -> None:
        for segment in self.snake:
            x, y = segment
            self.plansza[x][y] = 'Z'   
            
    def odswiezPlansze(self) -> None:
        
        self.wygenerujPlansze()
        
        for x, y in self.owoce:
            self.plansza[x][y] = 'O'
        
        for x, y in self.snake:
            self.plansza[x][y] = 'X'    
    
    
     
            
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
    "[][X][X]\n"
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
    "[X][][]\n"
    "[X][X][]\n"
)


print(waz2.planszaNaString())
print(spodziewanaPlansza2)

assert waz2.planszaNaString() == spodziewanaPlansza2 , "Planasza zgadza się z spodziewaną"
assert waz2.ileZjedzonychOwockow() == 2


#nowa gra3
#---Test3---

ruchyDoWykonania3: List[str] = ["d", "d", "s", "s", "a", "a", "w", "d"]
waz3: Snake = Snake(ruchyDoWykonania3)
waz3.wygenerujPlansze()
waz3.wygenerujSnake(0, 0)
waz3.postawOwoc(1, 2)
waz3.postawOwoc(2, 0)
waz3.postawOwoc(1, 0)
waz3.postawOwoc(1, 1)



poczatkowaPlansza3: str = (
    "[X][][]\n"
    "[O][O][O]\n"
    "[O][][]\n"
)

assert waz3.planszaNaString() == poczatkowaPlansza3

waz3.wykonajRuchy()

spodziewanaPlansza3: str = (
    "[][][]\n"
    "[X][X][]\n"
    "[X][X][X]\n"
)


print(waz3.planszaNaString())
print(spodziewanaPlansza3)

assert waz3.planszaNaString() == spodziewanaPlansza3 , "Planasza zgadza się z spodziewaną"
assert waz3.ileZjedzonychOwockow() == 4
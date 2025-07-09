# metoda wygenerowania planszy 3x3
# metoda wywołania snake
# metoda wywołania owoców (jako punkty)
# metoda zbierająca/przechowywująca punkty
# metoda ruchu snake
# metoda rozbicia się snake o ogon lub plansze
# metoda gdzie przekonwertuje plansze na string
# metoda z klawiszami ruszam się ja

import random
from typing import List

class Snake:
    def  __init__(self, ruchyDoWykonania: List[str]) -> None:
        self.rozmiar: int = 3
        self.plansza: List[List[str]] = []
        self.snake: List[List[int]] = []
        self.owoce: List[List[int]] = []
        self.koniecGry: bool = True
        self.punkty: int = 0
        self.ruchy: List[str] = ruchyDoWykonania
        
        self.wygenerujPlansze()
        self.wygenerujSnake()
        self.wygenerujOwoce()
        
    
    def wygenerujPlansze(self) -> None:
        self.plansza = []
        
        for _ in range(self.rozmiar):
            wiersz: List[str] = []
            
            for _ in range(self.rozmiar):
                wiersz.append(' ')
                
            self.plansza.append(wiersz)

    def wygenerujSnake(self) -> None:
        x: int = 0
        y: int = 0
        
        self.snake =[[x, y]]
        self.plansza[x][y] = 'X'
        
    def wygenerujOwoce(self) -> None:
        self.owoce = []
        
        liczbaOwocow: int  = 1
        
        for _ in range(liczbaOwocow):
            while True:
                x = random.randint(0, self.rozmiar - 1)
                y = random.randint(0, self.rozmiar - 1)
                
                if self.plansza[x][y] == ' ':
                    self.plansza[x][y] = 'O'    
                    self.owoce.append([x, y])
                    break
                
    def dodajPunkty(self) -> None:
        self.punkty += 1
        
    def wykonajRuchy(self) -> None:
        
        for kierunek in self.ruchy:
            if self.koniecGry:
                break
            
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
            
            self.ruszajSnake(x, y)
            
    def ruszajSnake(self, x: int, y:int ) -> None:
        glowa = self.snake[0]
        
        nowyX = glowa[0] + x
        nowyY = glowa[1] + y
        
        if nowyX < 0:
            self.koniecGry = True
            return
        
        if nowyX >= self.rozmiar:
            self.koniecGry = True
            return
        
        if nowyY < 0:
            self.koniecGry = True
            return
        
        if nowyY >= self.rozmiar:
            self.koniecGry = True
            return
        
        for czescSnake in self.snake:
            if czescSnake[0] == nowyX and czescSnake[1] == nowyY:
                self.koniecGry = True
                return
            
        self.snake.insert(0, [nowyX, nowyY])
        
        if [nowyX, nowyY] in self.owoce:
            self.dodajPunkty()
            self.owoce.remove([nowyX, nowyY])
            self.wygenerujOwoce()
            
        else:
            self.snake.pop()
        
        self.aktualizujPlansze()
        
    def aktualizujPlansze(self) -> None:
        self.wygenerujPlansze()
        
        for owoc in self.owoce:
            x = owoc[0]
            y = owoc[1]
            self.plansza[x][y] = 'O'
            
        for segmentSnake in self.snake:
            x = segmentSnake[0]
            y = segmentSnake[1]
            self.plansza[x][y] = 'X'
            
        if self.koniecGry:
            x = self.snake[0][0]
            y = self.snake[0][1]
            self.plansza[x][y] = 'Z'
        
        
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
                    
            #robi x
            #dodaj nowa linia \n  
        
        
# --- TEST ---
waz = Snake(['d', 'd', 's', 'a', 'a', 'w'])
waz.wykonajRuchy()

planszadoTestow = waz.planszaNaString()


assert planszadoTestow.count('[O]') == 1, "Na planszy powinien być jeden owoc!"


assert '[Z]' not in planszadoTestow, "Wąż nie powinien zginąć!"

print("[OK] Test przeszedł!")



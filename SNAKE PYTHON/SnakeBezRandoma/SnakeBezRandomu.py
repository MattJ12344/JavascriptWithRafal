
from typing import List

class Snake:
    
    # Konstruktor
    def  __init__(self) -> None:
        self.rozmiar: int = 3
        self.plansza: List[List[str]] = []
        self.snake: List[List[int]] = []
        self.owoce: List[List[int]] = []
        self.punkty: int = 0
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
        
    def wykonajRuchy(self, ruchyDoWykonania: List[str]) -> None:
        
        for kierunek in ruchyDoWykonania:
            
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
            



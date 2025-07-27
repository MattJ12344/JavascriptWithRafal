
from typing import List

class Snake:
    
    # Konstruktor
    def  __init__(self, rozmiar:int ) -> None:
        self.rozmiar = rozmiar
        self.plansza: List[List[str]] = []
        self.snake: List[List[int]] = []
        self.owoce: List[List[int]] = []
        self.punkty: int = 0
        self.koniecGry: bool = False
        self.przeszkody: List[List[int]] = []
    
    
    def wygenerujPlansze(self) -> None:
        self.plansza = []
        
        for _ in range(self.rozmiar):
            wiersz: List[str] = []
            
            for _ in range(self.rozmiar):
                wiersz.append(' ')
                
            self.plansza.append(wiersz)

    def wygenerujSnake(self, x:int, y: int) -> None:
        
        if 3<= self.rozmiar <= 4:
            dlugosc: int = 1
            
        elif 5 <= self.rozmiar <=9:
            dlugosc:int  = 2
            
        elif 10 <= self.rozmiar <= 20:
            dlugosc:int = 3
            
        else:
            dlugosc:int = 1
            
        self.snake = []
        
        for i in range(dlugosc):
            nowyX:int = x
            nowyY:int = y + i
            
            if nowyY < self.rozmiar:
                self.snake.append([nowyX, nowyY])
        
        self.odswiezPlansze()

    def zczytywanieZTerminala(self) ->None:
        while self.koniecGry == False:
            print("Wprowadz kierunek (w/W)(s/S)(a/A)(d/D): ")
            krok:str = input().strip()
            self.wykonajRuch(krok)
            print(self.planszaNaString())
            
    def dodajPrzeszkodeNaSrodek(self) -> None:
        srodek:int = self.rozmiar // 2
        self.przeszkody.append([srodek, srodek])
        self.plansza[srodek][srodek] = '#'

    def postawPrzeszkody(self, x:int, y:int) -> None:

        if self.rozmiar < 5:
            print("Plansza za mala - przeszkody dozwolone od rozmiaru planszy 5x5")
            return

        if [x, y] in self.przeszkody:
            print(f"Przeszkoda juz istnieje na tym polu ({x}, {y})")
            return

        if [x, y] in self.przeszkody:
            print(f"Tu jest waz. Nie mozna wstawic przeszkody ({x}, {y})")
            return

        self.przeszkody.append([x, y])
        self.plansza[x][y] = '#'

        
    def postawOwoc(self, x:int, y:int) -> None:
        if [x, y] not in self.przeszkody:
            self.owoce.append([x, y])
            self.plansza[x][y] = 'O'
    
    def ileZjedzonychOwockow(self) -> int:
        return self.punkty
        
    def dodajPunkty(self) -> None:
        self.punkty += 1
        
    def wsadToKierunek(self, kierunek:str) -> List[int]:
        
        if kierunek == 'w' or kierunek == 'W':
                x:int = -1 
                y:int = 0
                
        elif kierunek == 's' or kierunek == 'S':
                x:int = 1 
                y:int = 0
                
        elif kierunek == 'a' or kierunek == 'A':
                x:int = 0 
                y:int = -1
            
        elif kierunek == 'd' or kierunek == 'D':
                x:int = 0 
                y:int = 1
                
        else:
            raise Exception("Nieprawidłowa literka ze wsadToKierunek wpisz wsad", kierunek)

        glowa: List[int]=  self.snake[len(self.snake) - 1]
            
        glowaX = glowa[0]
        glowaY = glowa[1]
            
        nowyX:int = (glowaX + x) % self.rozmiar
        nowyY:int = (glowaY + y) % self.rozmiar
        
        return [nowyX, nowyY]

    def wykonajRuch(self, ruchDoWykonania: str) -> None:
        self.wykonajRuchy([ruchDoWykonania])
        
    def wykonajRuchy(self, ruchyDoWykonania: List[str]) -> None:
        
        for kierunek in ruchyDoWykonania:

            kierunki:List[int] = self.wsadToKierunek(kierunek)
            
            nowyX:int = kierunki[0]
            nowyY:int = kierunki[1]
            
            #szuka czy napotka czesc ciala i wtedy ma się zakonczyc gre
            if [nowyX, nowyY] in self.snake: 
                self.koniecGry = True
                self.oznaczZakonczonaGre()
                return
            
            if [nowyX, nowyY] in self.przeszkody: 
                self.koniecGry = True
                self.oznaczZakonczonaGre()
                return
            
            self.snake.append([nowyX, nowyY])
            
            if [nowyX, nowyY] in self.owoce:
                self.owoce.remove([nowyX, nowyY])
                self.dodajPunkty()
            
            else:
                self.snake.pop(0)
                
            self.odswiezPlansze()

    
    def oznaczZakonczonaGre(self) -> None:
        for segment in self.snake:
            x: int = segment[0]
            y: int = segment[1]
            self.plansza[x][y] = 'Z'   
            
            
    def odswiezPlansze(self) -> None:
        
        for i in range(self.rozmiar):
            for j in range(self.rozmiar):
                if self.plansza[i][j].isdigit() or self.plansza == 'O':
                    self.plansza[i][j] = ' '
        
        for x, y in self.owoce:
            if [x, y] not in self.przeszkody:
                self.plansza[x][y] = 'O'
            
        for x, y in self.przeszkody:
            self.plansza[x][y] = '#'
        
        for i, (x, y) in enumerate(reversed(self.snake)):
            self.plansza[x][y] = str(i + 1)    
    
    
    def planszaNaString(self) -> str:
        wynik:str = ""
        
        for wiersz in self.plansza:
            
            for pole in wiersz:
                
                if pole == ' ':
                    wynik = wynik + "[ ]"
                    
                else:
                    wynik = wynik + f"[{pole}]"
                    
            wynik = wynik + "\n"
            
        return wynik
            



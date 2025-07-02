# metoda z graczami będzie dwóch graczy player 1 i palyer 2
# metoda gdzie tworzy plansze 3 x 3 
# metoda z wygraną i przegraną graczy : aby wygrać, trzeba mieć 3 wygrane
# metoda przechowująca dane graczy
# metoda sprawdzająca, aby gracze nie dawali swoich znaków na przeciwnego gracza znak
# gracze x lub o, że x zaczyna pierwszy gracz, który ma x 
# konstruktor z danymi

import random
from typing import List, Optional


class KolkoIKrzyzyk:
    def __init__(self) -> None:
        self.rozmiar: int = 5
        self.plansza: List[List[str]] = []
        self.gracze: List[str] = ['X', 'O']
        self.wygrany: Optional[str] = None
        self.punkty: dict[str, int] = {'X': 0, 'O': 0}
        self.utworzPustaPlansze()
        self.rozpocznijGre()

    def utworzPustaPlansze(self) -> None:
        self.plansza = []
        
        for i in range(self.rozmiar):
            wiersz: List[str] = []
            
            for j in range(self.rozmiar):
                wiersz.append(' ')
                
            self.plansza.append(wiersz)
    
    
    def wyswietlPlansze(self)-> None:
        for wiersz in self.plansza:
            print(' | '.join(wiersz))
        
        print('-' * (self.rozmiar * 4 - 1))
        
    
    def znajdzWolnePole(self) -> List[int]:
        wolnePola: List[List[int]] = []
        
        for i in range(self.rozmiar):
            for j in range(self.rozmiar):
                if self.plansza[i][j] == ' ':
                    wolnePola.append([i, j])
        
        return random.choice(wolnePola)
        
        
    
    def wykonajRuch(self, gracz: str) -> None:
        pole: List[int] = self.znajdzWolnePole()
        
        x = pole[0]
        y = pole[1]
        
        self.plansza[x][y] = gracz
        
    def sprawdzWygrana(self, gracz: str) -> bool:
        
        wymagane:int = 5
        
        for i in range(self.rozmiar):
            
            for j in range(self.rozmiar - wymagane + 1):

                
                wszystkie = True
                for k in range(wymagane):
                    
                    if self.plansza[i][j + k] != gracz:
                        wszystkie = False
                        break
                if wszystkie:
                    
                    return True

                
                wszystkie = True
                for k in range(wymagane):
                    
                    if self.plansza[j + k][i] != gracz:
                        wszystkie = False
                        break
                    
                if wszystkie:
                    return True

        
        for i in range(self.rozmiar - wymagane + 1):
            
            for j in range(self.rozmiar - wymagane + 1):
                
                wszystkie = True
                
                for k in range(wymagane):
                    
                    if self.plansza[i + k][j + k] != gracz:
                        wszystkie = False
                        break
                    
                if wszystkie:
                    return True

        
        for i in range(self.rozmiar - wymagane + 1):
            
            for j in range(wymagane - 1, self.rozmiar):
                wszystkie = True
                
                for k in range(wymagane):
                    if self.plansza[i + k][j - k] != gracz:
                        wszystkie = False
                        break
                    
                if wszystkie:
                    return True

        return False

    def czyJestRemis(self) -> bool:
        for i in range(self.rozmiar):
            
            for j in range(self.rozmiar):
                
                if self.plansza[i][j] == ' ':
                    return False
        
        return True
            
    def zresetujRundeGry(self) -> None:
        self.utworzPustaPlansze()
        self.wygrany = None
        
    
    def rozpocznijGre(self) -> None:
        print("Start gry pomiedzy dwoma graczami")
        
        licznikRund: int = 0
        
        while self.punkty['X'] < 3 and self.punkty['O'] < 3:
            self.zresetujRundeGry()
            
            if licznikRund % 2 == 0:
                gracz = 'X'
            else:
                gracz = 'O'
            
            print(f"\n--- Runda {licznikRund + 1} ---")
            
            while True:
                self.wykonajRuch(gracz)
                
                if self.sprawdzWygrana(gracz):
                    self.wygrany = gracz
                    self.punkty[gracz] += 1
                    break
                    
                
                if self.czyJestRemis():
                    break
                    
                
                if gracz == 'X':
                    gracz = 'O'
                    
                else:
                    gracz = 'X'
                    
                    
            
            print("\n Plansza po rundzie: ")
            self.wyswietlPlansze()
            
            if self.wygrany != None:
                print(f"Gracz {self.wygrany} wygral runde!")
                
            else:
                print("Remis!")
                
            print(f"Wynik: X = {self.punkty['X']} | O = {self.punkty['O']}\n")
            
            licznikRund += 1
            
            
        if self.punkty['X'] == 3:
            print("Gracz X wygral cala gre!")
            
        else:
            print("Gracz O wygral cala gre!")     


gra = KolkoIKrzyzyk()

gra.rozpocznijGre()
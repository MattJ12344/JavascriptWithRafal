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

    def utworzPustaPlansze(self) -> None:
        self.plansza = []
        
        for _ in range(self.rozmiar):
            wiersz: List[str] = []
            
            for _ in range(self.rozmiar):
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
        
    def czyWygranaWiersz(self, gracz: str) -> bool:
        
        for i in range(self.rozmiar):
            wszystkie = True
            for j in range(self.rozmiar):
                if self.plansza[i][j] != gracz:
                        wszystkie = False
                        break
            if wszystkie:
                return True
        return False

    def czyWygranaKolumna(self, gracz: str) -> bool:         
        for i in range(self.rozmiar):
            wszystkie = True
            for j in range(self.rozmiar):
                if self.plansza[j][i] != gracz:
                        wszystkie = False
                        break
            if wszystkie:
                return True
        return False


    def czyWygranaSkosLewy(self, gracz: str) -> bool:    
        for i in range(self.rozmiar):
             
            if self.plansza[i][i] != gracz:
                return False
        return True

    def czyWygranaSkosPrawy(self, gracz: str) -> bool:
        for i in range(self.rozmiar):
             
            if self.plansza[i][self.rozmiar - 1- i] != gracz:
                return False
        return True

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
        
        licznikGier: int = 0
        
        while self.punkty['X'] < 3 and self.punkty['O'] < 3:
            self.zresetujRundeGry()
            
            if licznikGier % 2 == 0:
                gracz = 'X'
            else:
                gracz = 'O'
            
            print(f"\n--- Runda {licznikGier + 1} ---")
            
            while True:
                self.wykonajRuch(gracz)
                
                if (
                    self.czyWygranaWiersz(gracz)
                    or self.czyWygranaKolumna(gracz)
                    or self.czyWygranaSkosLewy(gracz)
                    or self.czyWygranaSkosPrawy(gracz)
                ):
                    self.wygrany = gracz
                    self.punkty[gracz] +=1
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
            
            licznikGier += 1
            
            
        if self.punkty['X'] == 3:
            print("Gracz X wygral cala gre!")
            
        else:
            print("Gracz O wygral cala gre!")     


gra = KolkoIKrzyzyk()

gra.rozpocznijGre()
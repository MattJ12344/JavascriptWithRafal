# // ### ZADANIE OD RAFAŁA
# // ZROUMIEĆ W PEŁNI gracz1/gracz2/aktualnyGracz i metody, które można wywołać na nich
# // zdebuguj dokładnie okolice lini "this.aktualnyGracz.pokazPlanszeAtaku();"

# // jeśli gracz trafi statek to wtedy gracz, który trafił może jeszce raz strzelić [trafiony zatopiny] (if), zmienić gracza, jeśli nie trafił (else)
# // posprawdzaj za pomocą ctrl+spacja co możesz użyć np. this.aktualnyGracz.<ctrl+spacja>

# // #### UMIESZCZANIE STATKÓW - ZROBIĆ NA SAMYM KOŃCU
# // - Potem dodam rozszerzę tablice o 4x4 i dodam jednego 4, dwie 3, trzy 2 i cztery 1
# // - jeśli mi to wyjdzie to wtedy, robię 10x10 tablice w statkach



# // #### WYGRYWANIE - ZROBIĆ NA SAMYM KOŃCU
# // - może zrobię wygraną jak w kółko i krzyżyk, że dopiero po 3 zwycięstwach jest


# // MVP - Most Valuable Player
# // MVP - Minimal Value Product

import random

class Gracz:
    def __init__(self, nazwa: str, statki: list):
        self.plansza = self.utworz_pusta_plansze(10)
        self.plansza_ataku = self.utworz_pusta_plansze(10)
        self.statki = statki
        self.numer_tury = 0
        self.zajete_pola = []
        self.nazwa = nazwa
        self.rozmiar_planszy = 10

    def utworz_pusta_plansze(self, rozmiar: int) -> list:
        return [[' ' for _ in range(rozmiar)] for _ in range(rozmiar)]

    def czy_mozna_rozmiescic_statek(self, x: int, y: int, rozmiar: int, orientacja: str) -> bool:
        if orientacja == 'poziomo' and y + rozmiar > self.rozmiar_planszy:
            return False
        if orientacja == 'pionowo' and x + rozmiar > self.rozmiar_planszy:
            return False

        for i in range(rozmiar):
            pole_x = x + i if orientacja == 'pionowo' else x
            pole_y = y if orientacja == 'pionowo' else y + i

            if self.plansza[pole_x][pole_y] != ' ':
                return False
            if not self.czy_pole_jest_dostepne_z_odstepem(pole_x, pole_y):
                return False

        return True

    def czy_pole_jest_dostepne_z_odstepem(self, x: int, y: int) -> bool:
        kierunki = [-1, 0, 1]

        for sx in kierunki:
            for sy in kierunki:
                zx = x + sx
                zy = y + sy
                if 0 <= zx < self.rozmiar_planszy and 0 <= zy < self.rozmiar_planszy:
                    if self.plansza[zx][zy] != ' ':
                        return False
        return True

    def rozmiesc_statek(self, rozmiar: int, x: int, y: int, orientacja: str) -> None:
        if self.czy_mozna_rozmiescic_statek(x, y, rozmiar, orientacja):
            for i in range(rozmiar):
                pole_x = x + i if orientacja == 'pionowo' else x
                pole_y = y if orientacja == 'pionowo' else y + i
                self.plansza[pole_x][pole_y] = 'X'
                self.zajete_pola.append((pole_x, pole_y))
        else:
            print("Nie można umieścić statku w tej pozycji.")

    def pokaz_plansze(self) -> None:
        print(f"\n {self.nazwa} - Plansza:")
        for wiersz in self.plansza:
            print(' | '.join(wiersz))

    def pokaz_plansze_ataku(self) -> None:
        print(f"\n {self.nazwa} - Plansza ataków:")
        for wiersz in self.plansza_ataku:
            print(' | '.join(wiersz))

    def atakuj(self, przeciwnik, x: int, y: int) -> bool:
        print(f"{self.nazwa} atakuje pozycję ({x}, {y})")
        if przeciwnik.plansza[x][y] == 'X':
            print("Trafiony!")
            self.plansza_ataku[x][y] = 'Z'
            przeciwnik.plansza[x][y] = 'Z'
            return True
        else:
            print("Pudło.")
            self.plansza_ataku[x][y] = 'O'
            return False

    def czy_wszystkie_statki_zatopione(self) -> bool:
        return all(self.plansza[x][y] == 'Z' for x, y in self.zajete_pola)


class Statki:
    def __init__(self):
        self.gracz1 = Gracz("Gracz 1", [])
        self.gracz2 = Gracz("Gracz 2", [])
        self.aktualny_gracz = self.gracz1
        self.przeciwnik = self.gracz2
        self.licznik_gier = 0

    def zmien_gracza(self) -> None:
        self.aktualny_gracz, self.przeciwnik = self.przeciwnik, self.aktualny_gracz

    def losuj_pozycje_statku(self, rozmiar):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            orientacja = random.choice(['poziomo', 'pionowo'])
            if self.aktualny_gracz.czy_mozna_rozmiescic_statek(x, y, rozmiar, orientacja):
                return x, y, orientacja


    def rozmiesc_statki_autonomicznie(self, gracz) -> None:
        statki_do_rozmieszczenia = [
            4,  
            3, 3,  
            2, 2, 2,  
            1, 1, 1, 1  
        ]

        for rozmiar in statki_do_rozmieszczenia:
            x, y, orientacja = self.losuj_pozycje_statku(rozmiar)
            gracz.rozmiesc_statek(rozmiar, x, y, orientacja)
        gracz.pokaz_plansze()
    
    def losuj_pozycje_do_ataku(self, gracz):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if gracz.plansza_ataku[x][y] == ' ':
                return x, y

    def graj(self) -> None:

        print("Rozpoczynamy grę!")
        print("Gracz 1 rozmieszcza statki.")
        self.rozmiesc_statki_autonomicznie(self.gracz1)
        print("Gracz 2 rozmieszcza statki.")
        self.rozmiesc_statki_autonomicznie(self.gracz2)


        while True:
            print(f"\nTura {self.aktualny_gracz.nazwa}")
            self.aktualny_gracz.pokaz_plansze_ataku()
            x, y = self.losuj_pozycje_do_ataku(self.aktualny_gracz)

            self.aktualny_gracz.atakuj(self.przeciwnik, x, y)

            if self.przeciwnik.czy_wszystkie_statki_zatopione():
                if self.licznik_gier % 2 == 0:
                    print(f"{self.gracz1.nazwa} wygrywa! Wszystkie statki przeciwnika zatopione.")
                else:
                    print(f"{self.gracz2.nazwa} wygrywa! Wszystkie statki przeciwnika zatopione.")
                break
            self.zmien_gracza()
        
        self.licznik_gier += 1

if __name__ == "__main__":
    gra = Statki()
    gra.graj()

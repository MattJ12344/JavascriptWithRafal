class Gracz:
    def __init__(self, nazwa: str, statki: list):
        self.plansza = self.utworz_pusta_plansze(10)  
        self.plansza_ataku = self.utworz_pusta_plansze(10)  
        self.statki = statki
        self.numer_tury = 0
        self.zajete_pola = []
        self.nazwa = nazwa

    def utworz_pusta_plansze(self, rozmiar: int) -> list:
        return [[' ' for _ in range(rozmiar)] for _ in range(rozmiar)]

    def czy_mozna_rozmiescic_statek(self, x: int, y: int, rozmiar: int, orientacja: str) -> bool:
        if orientacja == 'poziomo' and y + rozmiar > 10:  
            return False
        if orientacja == 'pionowo' and x + rozmiar > 10:  
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
                if 0 <= zx < 10 and 0 <= zy < 10:  # Zmieniamy na 10x10
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

    def zmien_gracza(self) -> None:
        self.aktualny_gracz, self.przeciwnik = self.przeciwnik, self.aktualny_gracz

    def wybierz_statek_i_umiesc(self, gracz) -> None:
        # Lista statków do rozmieszczenia
        statki_do_rozmieszczenia = [
            4,  
            3, 3,  
            2, 2, 2,  
            1, 1, 1, 1  
        ]

        for rozmiar in statki_do_rozmieszczenia:
            while True:
                print(f"{gracz.nazwa}, wybierz pozycję dla statku o rozmiarze {rozmiar}:")
                x = int(input("Podaj pozycję x (0-9): "))
                y = int(input("Podaj pozycję y (0-9): "))
                orientacja = input("Podaj orientację (poziomo/pionowo): ")

                if gracz.czy_mozna_rozmiescic_statek(x, y, rozmiar, orientacja):
                    gracz.rozmiesc_statek(rozmiar, x, y, orientacja)
                    gracz.pokaz_plansze()
                    break
                else:
                    print("Nie można umieścić statku w tej pozycji, spróbuj ponownie.")

    def graj(self) -> None:
        print("Rozpoczynamy grę!")
        print("Gracz 1 rozmieszcza statki.")
        self.wybierz_statek_i_umiesc(self.gracz1)
        print("Gracz 2 rozmieszcza statki.")
        self.wybierz_statek_i_umiesc(self.gracz2)

        while True:
            print(f"\nTura {self.aktualny_gracz.nazwa}")
            self.aktualny_gracz.pokaz_plansze_ataku()
            x = int(input(f"{self.aktualny_gracz.nazwa}, podaj pozycję x do ataku (0-9): "))
            y = int(input(f"{self.aktualny_gracz.nazwa}, podaj pozycję y do ataku (0-9): "))

            if self.aktualny_gracz.atakuj(self.przeciwnik, x, y):
                if self.przeciwnik.czy_wszystkie_statki_zatopione():
                    print(f"{self.aktualny_gracz.nazwa} wygrywa! Wszystkie statki przeciwnika zatopione.")
                    break
            else:
                self.zmien_gracza()


if __name__ == "__main__":
    gra = Statki()
    gra.graj()
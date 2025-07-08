plansza = [
    ['X', '', 'O', 'O'],
    ['', '', '', 'O'],
    ['', '', '', 'O']
]

wierszDoUsuniecia =0

wiersz: int
dlugoscPlanszy: int = len(plansza)
for wiersz in range(dlugoscPlanszy):
    print("wiersz: ", wiersz)
    for i in range(len(plansza[wiersz])):
        print("i: ", i)
        if plansza[wiersz][i] == 'X':
            wierszDoUsuniecia = wiersz
            break


plansza[wierszDoUsuniecia].remove('X') 

print("plansza: ", plansza )

# zadanie to samo z remove
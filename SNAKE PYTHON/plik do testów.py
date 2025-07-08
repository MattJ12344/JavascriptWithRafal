
plansza = [
    ['X', '', 'O', 'O'],
    ['', '', '', 'O'],
    ['', '', '', 'O']
]

wierszDoUsuniecia =0
iDoUsuniecia =0

wiersz: int
dlugoscPlanszy: int = len(plansza)
for wiersz in range(0, dlugoscPlanszy):
    print("wiersz: ", wiersz)
    for i in range(0, len(plansza[wiersz])):
        print("i: ",  i)
        if plansza[wiersz][i] == 'X':
            wierszDoUsuniecia = wiersz
            iDoUsuniecia = i
            
plansza[wierszDoUsuniecia].pop(iDoUsuniecia) 
    
        
print("plansza: ", plansza )
    
                    
# zrobic to samo z remove
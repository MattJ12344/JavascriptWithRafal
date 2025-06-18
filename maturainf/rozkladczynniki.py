def wypisz_czynniki_pierwsze(liczba):
    n = liczba
    if n > 1:
        i = 2
        while i <= n:
            if n%i == 0:
                print(str(i)+";")
                n //= i
            else:
                i += 1
    return
    
wypisz_czynniki_pierwsze(1050403310)
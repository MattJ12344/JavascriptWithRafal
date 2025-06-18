def wydaj_reszte(reszta):
    dostepne = [10, 5, 2, 1] 
    monety = []
    
    for i in range(4):
        while(dostepne[i] <= reszta):
            reszta -= dostepne[i]
            monety.append(dostepne[i])
        
    for i in range(len(monety)):
        print(monety[i], end = '')
        
        if(i != len(monety) - 1):
            print(";", end= '')
            

wydaj_reszte(500-123)
        
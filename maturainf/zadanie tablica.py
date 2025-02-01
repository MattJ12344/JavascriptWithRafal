with open("tablica.txt", "r", encoding='utf-8') as f:
        wszystkie_slowa = []
        
        for line in f:
            slowa = line.split()

            if len(slowa) > 0:
               slowa[0] = slowa[0].lower()
            if len(slowa) > 1:
               slowa[1] = slowa[1].upper()
               
            for i in range(2, len(slowa)):
                slowa[i] = slowa[i].swapcase()
            
            wszystkie_slowa.extend(slowa)
            

print(";".join(wszystkie_slowa))
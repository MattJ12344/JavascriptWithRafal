from collections import deque

with open('suma.txt', 'r') as file:
    K = int(file.readline())  
    ciag = list(map(int, file.readline().split()))  

kolejka = deque()
suma = 0
wynik = 0

for i in ciag:
    kolejka.append(i)
    suma += i
    
    while suma > K:
        x = kolejka.popleft() 
        suma -= x
    wynik = max(wynik, suma)

print(wynik)
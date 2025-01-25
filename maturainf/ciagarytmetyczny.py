with open('daneciag.txt', 'r') as plik:
    wejscie = plik.read().split()
    
l = [int(x) for x in wejscie]
n = len(l)
    
w = 1

for a in range(n): 
    for b in range(a+1, n): 
        dl = 2
        ostatni = b
        for c in range(b+1, n): 
            if l[c] == l[ostatni] + l[b] - l[a]:
                dl += 1
                ostatni = c
        w = max(w, dl)
print(w)
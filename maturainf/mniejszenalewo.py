with open('mniejsza_na_lewo.txt', 'r') as plik:
    n = int(plik.readline().strip())
    l = list(map(int, plik.readline().strip().split()))
    
for i in range(n):
	w = -1
	for j in range(i):
		if l[j] < l[i]:
			w = max(w, l[j])
			
	print(w, end=' ')
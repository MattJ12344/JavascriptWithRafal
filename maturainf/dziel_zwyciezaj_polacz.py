def polacz(a, b):
	a_index, b_index = 0, 0
	a_len, b_len = len(a), len(b)
	c = []
	while a_index < a_len and b_index < b_len:
		if a[a_index] <= b[b_index]:
			c.append(a[a_index])
			a_index += 1
		else:
			c.append(b[b_index])
			b_index += 1
   
	while a_index != a_len:
		c.append(a[a_index])
		a_index += 1
	while b_index != b_len:
		c.append(b[b_index])
		b_index += 1
	
	return c

def zwyciezaj(t, a, b):
	if a == b:
     
		return [t[a]]
	else:
		sr = (a+b)//2
		return polacz(zwyciezaj(t, a, sr), zwyciezaj(t, sr + 1, b))

with open('Liczby_dziel_zwyciezaj.txt', 'r') as f:
    arr = f.read()

l = list(map(int, arr.split()))
wynik = zwyciezaj(l, 0, len(l) - 1)
sr = (len(wynik) - 1) // 2

print(wynik[sr])
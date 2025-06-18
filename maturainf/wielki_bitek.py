def czy_pierwsza(n):
	k =2

	while k*k <= n:
		if n%k == 0:
			return False
		k += 1
	return True

counter = 0
i = 9999
while counter < 5:
    if(czy_pierwsza(i)):
        print(str(i) + "; ")
        counter+=1
    i-=1
l = 578
m = 1
while l > 9: 
    m += 1
    suma_cyfr = 0 
    while l != 0:
        suma_cyfr += l % 10
        l //= 10
    l = suma_cyfr 

print(m)
with open('odwrotna.txt', 'r') as file:
    dane = file.read().split() 
stos = []

for x in dane:
    if x in ['x', '+', '-', '/']:  
        a = stos.pop()
        b = stos.pop()
        if x == 'x':
            stos.append(a * b)
        elif x == '+':
            stos.append(a + b)
        elif x == '-':
            stos.append(b - a)
        else:
            stos.append(b // a)
    else:
        stos.append(int(x))

print(stos.pop())
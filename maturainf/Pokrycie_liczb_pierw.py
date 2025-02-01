with open("pokrycie.txt", "r") as f:
    n = int(f.readline().strip())
    
    ciag = set(map(int, f.readline().split()))
    
    pierwsza = [False, False] + [True] * (n - 1)
    
    odp = True
    
    for i in range(2, n + 1):
        if pierwsza[i]:
            if i not in ciag: 
                odp = False
                break
            k = 2
            while i * k <= n:
                pierwsza[i * k] = False
                k += 1
    
    if odp:
        print("TAK")
    else:
        print("NIE")
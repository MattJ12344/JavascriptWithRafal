with open("mosiek.txt", "r") as f:
    n, m = f.readline().split()
    n = int(n)
    m = int(m)
    
    s1 = set()
    s2 = set()
    
    for i in range(n):
        x = int(f.readline().strip())
        
        if(m - x) in s1:
            if x < (m - x):
                s2.add((x, m-x))
            else:
                s2.add((m-x, x))
        
        s1.add(x)
        
    print(len(s2))

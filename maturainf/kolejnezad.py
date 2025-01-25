def max_kilometers(kilometers):
    n = len(kilometers)
    
    if n == 0:
        return 0
    
    if n == 1:
        return kilometers[0]
   
    dp = [0] * n
    
    dp[0] = kilometers[0]
    dp[1] = max(kilometers[0], kilometers[1])
   
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + kilometers[i])
    
    return dp[-1]

with open("dane.txt", "r") as file:
    kilometers = list(map(int, file.read().split()))

print(max_kilometers(kilometers))
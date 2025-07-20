class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
    
    
sol = Solution()

assert sol.divisorGame(1) == False  
assert sol.divisorGame(2) == True   
assert sol.divisorGame(3) == False  
assert sol.divisorGame(4) == True   
assert sol.divisorGame(10) == True 


print("nuda")
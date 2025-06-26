import math

class Solution:
    def arrangeCoins(self, coins: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        
        return int((math.sqrt(8 * coins + 1) - 1) // 2)



sol = Solution()

assert sol.arrangeCoins(0) == 0      
assert sol.arrangeCoins(1) == 1      
assert sol.arrangeCoins(3) == 2      
assert sol.arrangeCoins(5) == 2      
assert sol.arrangeCoins(8) == 3      
assert sol.arrangeCoins(10) == 4     
assert sol.arrangeCoins(15) == 5     
assert sol.arrangeCoins(1804289383) == 60070  

print("TEST")
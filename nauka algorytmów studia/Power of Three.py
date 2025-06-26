class Solution(object):
    def isPowerOfThree(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return 1162261467 % n == 0
    
sol = Solution()

assert sol.isPowerOfThree(1) == True      
assert sol.isPowerOfThree(3) == True      
assert sol.isPowerOfThree(9) == True      
assert sol.isPowerOfThree(27) == True     
assert sol.isPowerOfThree(0) == False
assert sol.isPowerOfThree(-3) == False
assert sol.isPowerOfThree(45) == False
assert sol.isPowerOfThree(1162261467) == True  
assert sol.isPowerOfThree(1162261466) == False

print("nuda")
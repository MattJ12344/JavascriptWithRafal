class Solution(object):
    def isPowerOfFour(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        if n == 1:
            return True

        while n > 1:
            if n % 4 != 0:
                return False
            
            n //= 4

        return True        

sol = Solution()

assert sol.isPowerOfFour(1) == True      
assert sol.isPowerOfFour(4) == True      
assert sol.isPowerOfFour(16) == True     
assert sol.isPowerOfFour(64) == True     
assert sol.isPowerOfFour(5) == False
assert sol.isPowerOfFour(0) == False
assert sol.isPowerOfFour(-4) == False
assert sol.isPowerOfFour(8) == False
assert sol.isPowerOfFour(1024) == True 

print("Siema")
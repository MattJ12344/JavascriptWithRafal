class Solution(object):
    def isPowerOfTwo(self, n:int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0
    
sol = Solution()

assert sol.isPowerOfTwo(1) == True     
assert sol.isPowerOfTwo(2) == True     
assert sol.isPowerOfTwo(4) == True     
assert sol.isPowerOfTwo(16) == True    
assert sol.isPowerOfTwo(3) == False
assert sol.isPowerOfTwo(0) == False
assert sol.isPowerOfTwo(-2) == False
assert sol.isPowerOfTwo(218) == False

print("Zrobione")
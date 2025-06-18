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

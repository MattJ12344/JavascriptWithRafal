class Solution(object):
    def divide(self, dividend:int, divisor:int) -> int:
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1 
        
        if divisor == 1:
            return dividend
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        n, d: int = abs(dividend), abs(divisor)
        result:int = 0

        while n >= d:
            p:int = 0
            
            while n >= (d << p):
                p += 1
            
            p -= 1
            n -= (d << p)
            result += (1 << p)

        return min(max(sign * result, -2**31), 2**31 - 1)
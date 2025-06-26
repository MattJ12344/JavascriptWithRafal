class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1 
        
        if divisor == 1:
            return dividend
        
        sign: int = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        n: int = abs(dividend)
        d: int = abs(divisor)
        result: int = 0

        while n >= d:
            p: int = 0
            while n >= (d << p):
                p += 1
            p -= 1
            n -= (d << p)
            result += (1 << p)

        return min(max(sign * result, -2**31), 2**31 - 1)
    
sol = Solution()

assert sol.divide(10, 3) == 3
assert sol.divide(7, -3) == -2
assert sol.divide(0, 1) == 0
assert sol.divide(1, 1) == 1
assert sol.divide(-2**31, -1) == 2**31 - 1 
assert sol.divide(-2**31, 1) == -2**31
assert sol.divide(2**30, 2) == 2**29
assert sol.divide(-15, 4) == -3
assert sol.divide(15, -4) == -3
assert sol.divide(-15, -4) == 3

print("OKEJ!")
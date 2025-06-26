class Solution(object):
    def myAtoi(self, s: str) -> int:
        i: int = 0
        n: int = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign: int = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        result: int = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])

            if result * sign > 2**31 - 1:
                return 2**31 - 1
            if result * sign < -2**31:
                return -2**31

            i += 1

        return result * sign
    
sol = Solution()

assert sol.myAtoi("42") == 42
assert sol.myAtoi("   -42") == -42
assert sol.myAtoi("4193 with words") == 4193
assert sol.myAtoi("words and 987") == 0
assert sol.myAtoi("-91283472332") == -2147483648  # underflow
assert sol.myAtoi("91283472332") == 2147483647    # overflow
assert sol.myAtoi("+1") == 1
assert sol.myAtoi("") == 0
assert sol.myAtoi("00000-42a1234") == 0
assert sol.myAtoi("   +0 123") == 0

print("Zrobione again")
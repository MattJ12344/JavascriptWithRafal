class Solution(object):
    def titleToNumber(self, columnTitle: str) -> int:
        """
        :type columnTitle: str
        :rtype: int
        """
        result: int = 0
        
        for letter in columnTitle:
            result = result * 26 +(ord(letter) - 64)
            
        return result
    
sol = Solution()

assert sol.titleToNumber("A") == 1
assert sol.titleToNumber("Z") == 26
assert sol.titleToNumber("AA") == 27
assert sol.titleToNumber("AB") == 28
assert sol.titleToNumber("BA") == 53
assert sol.titleToNumber("ZY") == 701
assert sol.titleToNumber("FXSHRXW") == 2147483647  

print("Cudek dnia")
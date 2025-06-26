class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        :type s: str
        :rtype: int
        """
        result: str = ""

        while columnNumber > 0:
            columnNumber -= 1
            result = chr((columnNumber % 26) + ord("A")) + result
            columnNumber //= 26

        return result
    
sol = Solution()

assert sol.convertToTitle(1) == "A"
assert sol.convertToTitle(26) == "Z"
assert sol.convertToTitle(27) == "AA"
assert sol.convertToTitle(28) == "AB"
assert sol.convertToTitle(52) == "AZ"
assert sol.convertToTitle(53) == "BA"
assert sol.convertToTitle(701) == "ZY"
assert sol.convertToTitle(702) == "ZZ"
assert sol.convertToTitle(703) == "AAA"
assert sol.convertToTitle(704) == "AAB"

print("DWA")
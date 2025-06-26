class Solution(object):
    def addDigits(self, number: int) -> int:
        """
        :type num: int
        :rtype: int
        """
        if number == 0:
            return 0
        return 1 + (number - 1) % 9
    

sol = Solution()

assert sol.addDigits(38) == 2
assert sol.addDigits(0) == 0
assert sol.addDigits(190) == 1
assert sol.addDigits(10000000) == 1
assert sol.addDigits(389) == 2

print("cos")
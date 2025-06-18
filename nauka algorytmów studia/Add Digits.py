class Solution(object):
    def addDigits(self, number: int) -> int:
        """
        :type num: int
        :rtype: int
        """
        if number == 0:
            return 0
        return 1 + (number - 1) % 9
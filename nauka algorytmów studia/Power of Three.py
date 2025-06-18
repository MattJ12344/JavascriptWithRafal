class Solution(object):
    def isPowerOfThree(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return 1162261467 % n == 0
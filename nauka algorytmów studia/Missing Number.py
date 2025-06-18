class Solution(object):
    def missingNumber(self, numbers: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        count: int = len(numbers)
        
        expectedSum: int = count * (count + 1) // 2
        
        actualSum = sum(numbers)
        
        return expectedSum - actualSum
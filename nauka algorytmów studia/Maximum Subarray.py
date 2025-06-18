class Solution(object):
    def maxSubArray(self, numbers:list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        result:int = numbers[0]
        total:int = 0

        for index in numbers:
            if total < 0:
                total = 0

            total += index
            result = max(result, total)
        
        return result
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqNum = 0
        for idx in nums:
            uniqNum ^= idx
        return uniqNum  
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        current = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count = 0
                nums[current] = nums[i]
                current += 1
            else:
                count += 1
                if count <= 1:
                    nums[current] = nums[i]
                    current += 1
        return current
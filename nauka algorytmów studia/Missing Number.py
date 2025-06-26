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
    
sol = Solution()

assert sol.missingNumber([3, 0, 1]) == 2
assert sol.missingNumber([0, 1]) == 2
assert sol.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
assert sol.missingNumber([0]) == 1
assert sol.missingNumber([1]) == 0

print("Udało się")
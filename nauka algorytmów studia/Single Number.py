from typing import List

class Solution(object):
    def singleNumber(self, numbers: List[int]) -> int:
        """
        :type numbers: List[int]
        :rtype: int
        """
        unique_number: int = 0
        for number in numbers:
            unique_number ^= number
        return unique_number
    
sol = Solution()

assert sol.singleNumber([2, 2, 1]) == 1
assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
assert sol.singleNumber([1]) == 1
assert sol.singleNumber([0, 0, 100]) == 100
assert sol.singleNumber([99, 77, 99]) == 77

print("Check ")

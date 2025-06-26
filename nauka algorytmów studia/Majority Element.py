from typing import List

class Solution:
    def majorityElement(self, numbers: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numbers.sort()
        count: int = len(numbers)
        return numbers[count // 2]
    
sol = Solution()

assert sol.majorityElement([1]) == 1

assert sol.majorityElement([2, 2]) == 2

assert sol.majorityElement([3, 3, 4]) == 3

assert sol.majorityElement([1, 1, 1, 2, 3]) == 1

assert sol.majorityElement([6, 5, 6, 6]) == 6

assert sol.majorityElement([8, 8, 7, 8, 5, 8, 8]) == 8

print("Nuda")
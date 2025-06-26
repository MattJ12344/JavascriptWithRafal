from typing import List

class Solution(object):
    def search(self, numbers: List[int], target: int) -> int:
        """
        :type numbers: List[int]
        :type target: int
        :rtype: int
        """
        start: int = 0
        end: int = len(numbers) - 1

        while start <= end:
            middle: int = (start + end) // 2

            if target == numbers[middle]:
                return middle

            if numbers[start] <= numbers[middle]: 
                if numbers[start] <= target <= numbers[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            else:  
                if numbers[middle] <= target <= numbers[end]:
                    start = middle + 1
                else:
                    end = middle - 1

        return -1
    
sol = Solution()

# Test 1
assert sol.search([4,5,6,7,0,1,2], 0) == 4

# Test 2
assert sol.search([4,5,6,7,0,1,2], 3) == -1

# Test 3
assert sol.search([1,2,3,4,5,6], 4) == 3

# Test 4
assert sol.search([1], 1) == 0

# Test 5
assert sol.search([1], 0) == -1

# Test 6
assert sol.search([5,6,7,8,1,2,3], 3) == 6

print("KOD")
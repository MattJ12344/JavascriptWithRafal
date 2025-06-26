from typing import List

class Solution(object):
    def search(self, numbers: List[int], target: int) -> bool:
        """
        :type numbers: List[int]
        :type target: int
        :rtype: bool
        """
        left: int = 0
        right: int = len(numbers) - 1
        
        while left <= right:
            middle: int = (left + right) // 2
            
            if numbers[middle] == target:
                return True
            
            if numbers[middle] == numbers[left]:
                left += 1
                continue

            if numbers[left] <= numbers[middle]:
                if numbers[left] <= target < numbers[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
               
                if numbers[middle] < target <= numbers[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return False
    
sol = Solution()

# Test 1
assert sol.search([2,5,6,0,0,1,2], 0) == True

# Test 2
assert sol.search([2,5,6,0,0,1,2], 3) == False

# Test 3
assert sol.search([1,1,1,1,1,1], 1) == True

# Test 4
assert sol.search([1,1,1,1,1,1], 2) == False

# Test 5
assert sol.search([], 1) == False

# Test 6
assert sol.search([5], 5) == True

# Test 7
assert sol.search([5], 0) == False

# Test 8
assert sol.search([1,2,3,4,5,6], 4) == True

print("mama")
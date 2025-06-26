class Solution(object):
    def search(self, numbers:list[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left:int = 0
        right:int  = len(numbers) - 1
        
        while left <= right:
            
            mid:int = (left + right) // 2
            
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    

sol = Solution()

# Test 1:
assert sol.search([1, 3, 5, 7, 9], 5) == 2

# Test 2
assert sol.search([1, 3, 5, 7, 9], 1) == 0

# Test 3
assert sol.search([1, 3, 5, 7, 9], 9) == 4

# Test 4
assert sol.search([2, 4, 6, 8], 6) == 2

# Test 5
assert sol.search([1, 3, 5, 7, 9], 4) == -1

# Test 6
assert sol.search([], 10) == -1

# Test 7
assert sol.search([5], 5) == 0

# Test 8
assert sol.search([5], 3) == -1

print("lol")
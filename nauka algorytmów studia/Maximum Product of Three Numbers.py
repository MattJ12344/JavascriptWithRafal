from typing import List

class Solution(object):
    def maximumProduct(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = -1001
        min1 = min2 = 1001

        for x in nums:
            if x > max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x

            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

        return max(max1 * max2 * max3, min1 * min2 * max1)
    
sol = Solution()

assert sol.maximumProduct([1, 2, 3]) == 6  
assert sol.maximumProduct([1, 2, 3, 4]) == 24  
assert sol.maximumProduct([-10, -10, 1, 3, 2]) == 300  
assert sol.maximumProduct([-1, -2, -3]) == -6  
assert sol.maximumProduct([-1, -2, -3, -4]) == -6  
assert sol.maximumProduct([0, 0, 0]) == 0
assert sol.maximumProduct([0, -1, 3, 100]) == 0  
assert sol.maximumProduct([-100, -99, 1, 2, 3]) == 29700  
assert sol.maximumProduct([5, 4, -10, -20]) == 1000  

print("Nuda")
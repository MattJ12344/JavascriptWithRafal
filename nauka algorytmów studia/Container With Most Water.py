class Solution(object):
    def maxArea(self, height: list[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        maxi:int= 0
        left:int = 0
        right:int = len(height) - 1
    
        while(left < right):
            area:int = min(height[left], height[right]) * (right - left)
            maxi = max(maxi, area)

            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
    
        return maxi
    
sol = Solution()

assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert sol.maxArea([1,1]) == 1
assert sol.maxArea([4,3,2,1,4]) == 16
assert sol.maxArea([1,2,1]) == 2
assert sol.maxArea([2,3,4,5,18,17,6]) == 17

print("HEH")
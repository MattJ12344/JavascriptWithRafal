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
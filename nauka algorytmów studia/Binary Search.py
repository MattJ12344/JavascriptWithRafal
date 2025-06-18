class Solution(object):
    def search(self, numbers:List[int], target: int) -> int:
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
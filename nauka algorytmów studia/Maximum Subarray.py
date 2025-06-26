class Solution(object):
    def maxSubArray(self, numbers:list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        result:int = numbers[0]
        total:int = 0

        for index in numbers:
            if total < 0:
                total = 0

            total += index
            result = max(result, total)
        
        return result
    
sol = Solution()

assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6 

assert sol.maxSubArray([1,2,3,4]) == 10

assert sol.maxSubArray([-1,-2,-3,-4]) == -1  

assert sol.maxSubArray([5]) == 5

assert sol.maxSubArray([-1,2,3,-4,5,6,-7]) == 12  

print("HURA")
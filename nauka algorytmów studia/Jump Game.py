class Solution(object):
    def canJump(self, numbers: list[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal:int = len(numbers) - 1

        for i in range(len(numbers) - 2, -1, -1):
            
            if i + numbers[i] >= goal:
                goal = i
        
        return True if goal == 0 else False
    
sol = Solution()

assert sol.canJump([2, 3, 1, 1, 4]) == True     
assert sol.canJump([3, 2, 1, 0, 4]) == False    
assert sol.canJump([0]) == True               
assert sol.canJump([1, 0, 1, 0]) == False       
assert sol.canJump([2, 0, 0]) == True 

print("Maciek")
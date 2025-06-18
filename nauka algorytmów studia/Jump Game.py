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
class Solution(object):
    def nextPermutation(self, numbers: list[int]) -> None:
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index:int = len(numbers) - 2
        
        while index >= 0 and numbers[index] >= numbers[index + 1]:
            index -= 1

        if index >= 0:
            j = len(numbers) - 1
            
            while numbers[j] <= numbers[index]:
                j -= 1
                
            numbers[index], numbers[j] = numbers[j], numbers[index]


        numbers[index + 1:] = reversed(numbers[index + 1:])
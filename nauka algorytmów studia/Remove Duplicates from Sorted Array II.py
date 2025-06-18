class Solution(object):
    def removeDuplicates(self, numbers: list[int]) -> int :
        """
        :type nums: List[int]
        :rtype: int
        """
        count: int = 0
        currentNumbers:int = 1
        
        for i in range(1, len(numbers)):
            
            if numbers[i] != numbers[i - 1]:
                count = 0
                numbers[currentNumbers] = numbers[i]
                currentNumbers += 1
                
            else:
                count += 1
                if count <= 1:
                    numbers[currentNumbers] = numbers[i]
                    currentNumbers += 1
                    
                    
        return currentNumbers
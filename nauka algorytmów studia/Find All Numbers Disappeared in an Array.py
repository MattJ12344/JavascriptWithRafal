from typing import List

class Solution:
    def findDisappearedNumbers(self, numbers: List[int]) -> List[int]:
        """
        Zwraca listę brakujących liczb z zakresu 1..n w tablicy `numbers`.
        """
        size: int = len(numbers)
        
        for i in range(size):
            while numbers[i] != numbers[numbers[i] - 1]:
                numbers[numbers[i] - 1], numbers[i] = numbers[i], numbers[numbers[i] - 1]
        
        return [i + 1 for i in range(size) if numbers[i] != i + 1]


sol = Solution()

assert sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6]

assert sol.findDisappearedNumbers([1,2,3,4,5]) == []

assert sol.findDisappearedNumbers([1,1,1,1]) == [2,3,4]

assert sol.findDisappearedNumbers([]) == []

assert sol.findDisappearedNumbers([1]) == []

assert sol.findDisappearedNumbers([2]) == [1]

assert sol.findDisappearedNumbers([2,2]) == [1]

print("RAZ")
from typing import List

class Solution:
    def permute(self, numbers: List[int]) -> List[List[int]]:
        """
        :type numbers: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start: int) -> None:
            if start == len(numbers):
                result.append(numbers[:])
                return
            
            for i in range(start, len(numbers)):
                numbers[start], numbers[i] = numbers[i], numbers[start]
                backtrack(start + 1)
                numbers[start], numbers[i] = numbers[i], numbers[start]

        result: List[List[int]] = []
        backtrack(0)
        return result
    
sol = Solution()

assert sorted(sol.permute([1])) == [[1]]
assert sorted(sol.permute([1, 2])) == sorted([[1, 2], [2, 1]])
assert sorted(sol.permute([1, 2, 3])) == sorted([
    [1, 2, 3], [1, 3, 2],
    [2, 1, 3], [2, 3, 1],
    [3, 2, 1], [3, 1, 2]
])

print("Poprawiam")
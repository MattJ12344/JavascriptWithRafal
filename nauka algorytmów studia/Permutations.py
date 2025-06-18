class Solution(object):
    def permute(self, numbers: list[int]) -> list[list[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            if start == len(numbers):
                result.append(numbers[:])
                return
            
            for i in range(start, len(numbers)):
                numbers[start], numbers[i] = numbers[i], numbers[start]
                backtrack(start + 1)
                numbers[start], numbers[i] = numbers[i], numbers[start]

        result: list[list[int]] = []
        backtrack(0)
        return result
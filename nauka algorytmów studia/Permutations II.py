class Solution(object):
    def permuteUnique(self, numbers: list[int]) -> list[list[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations: list[list[int]] = []
        numbers.sort()
        self.dfs(numbers, [], permutations)
        return permutations
    
    def dfs(self, availableNumbers: list[int], currentPermutation: list[int], allPermutations: list[list[int]]) -> None:
        if not availableNumbers:
            allPermutations.append(currentPermutation)
            
        for index in range(len(availableNumbers)):
            
            if index > 0 and availableNumbers[index] == availableNumbers[index-1]:
                continue
            
            self.dfs(availableNumbers[:index]+availableNumbers[index+1:], currentPermutation+[availableNumbers[index]], allPermutations)
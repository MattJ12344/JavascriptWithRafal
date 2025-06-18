class Solution(object):
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start:int, target:int, path: list[int]) -> None:
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])

        result: list[list[int]]= []
        candidates.sort()
        backtrack(0, target, [])
        return result
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
    
sol = Solution()

res1 = sol.combinationSum([2, 3, 6, 7], 7)
expected1 = [[2, 2, 3], [7]]
assert sorted(map(sorted, res1)) == sorted(map(sorted, expected1))

res2 = sol.combinationSum([2, 3, 5], 8)
expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
assert sorted(map(sorted, res2)) == sorted(map(sorted, expected2))

res3 = sol.combinationSum([2], 1)
assert res3 == []

res4 = sol.combinationSum([1], 1)
assert res4 == [[1]]

print("NUDA")
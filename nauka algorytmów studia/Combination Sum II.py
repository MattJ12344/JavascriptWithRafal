class Solution(object):
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result: list[list[int]] = []
        candidates.sort()
        def dfs(startIndex: int, candidates: list[int], target:int, path:list[int], result: list[list[int]]) -> None:
            if target < 0:
                return 
            
            if target == 0:
                result.append([x for x in path])
                return
            
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                dfs(i + 1, candidates, target - candidates[i], path, result)
                path.pop()


        dfs(0, candidates, target, [], result)
        return result
    

sol = Solution()

res1 = sol.combinationSum2([10,1,2,7,6,1,5], 8)
expected1 = [[1,1,6],[1,2,5],[1,7],[2,6]]
assert sorted(map(sorted, res1)) == sorted(map(sorted, expected1))

res2 = sol.combinationSum2([2,5,2,1,2], 5)
expected2 = [[1,2,2],[5]]
assert sorted(map(sorted, res2)) == sorted(map(sorted, expected2))

res3 = sol.combinationSum2([1,1,1,1,1], 3)
expected3 = [[1,1,1]]
assert sorted(map(sorted, res3)) == sorted(map(sorted, expected3))

res4 = sol.combinationSum2([], 3)
assert res4 == []

print("TEST")
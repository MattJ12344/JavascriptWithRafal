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
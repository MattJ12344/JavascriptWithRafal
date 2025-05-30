class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        def dfs(s, candidates, target, path, ans):
            if target < 0:
                return 
            if target == 0:
                ans.append([x for x in path])
                return
            for i in range(s, len(candidates)):
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, candidates, target - candidates[i], path, ans)
                path.pop()

        dfs(0, candidates, target, [], ans)
        return ans
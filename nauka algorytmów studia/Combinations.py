class Solution(object):
    def combine(self, n:int, k:int) -> list[list[int]]:
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res: list[list[int]] = []
        comb: list[int] = []
    
        def backtrack(start:int) -> None:
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()

        backtrack(1)
        return res
    

sol = Solution()

res1 = sol.combine(4, 2)
expected1 = [
    [1,2], [1,3], [1,4],
    [2,3], [2,4],
    [3,4]
]
assert sorted(res1) == sorted(expected1)

res2 = sol.combine(1, 1)
assert res2 == [[1]]

res3 = sol.combine(3, 1)
expected3 = [[1], [2], [3]]
assert sorted(res3) == sorted(expected3)

res4 = sol.combine(3, 3)
assert res4 == [[1, 2, 3]]


print("Pisanie")
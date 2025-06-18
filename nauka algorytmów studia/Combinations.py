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
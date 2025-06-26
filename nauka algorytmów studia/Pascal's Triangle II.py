class Solution(object):
    def getRow(self, rowIndex: int) -> list[int]:
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row: list[int] = [1]

        for _ in range(rowIndex):
            row = [left + right for left, right in zip([0]+row, row+[0])]
            
        return row    
    
sol = Solution()

assert sol.getRow(0) == [1]
assert sol.getRow(1) == [1, 1]
assert sol.getRow(2) == [1, 2, 1]
assert sol.getRow(3) == [1, 3, 3, 1]
assert sol.getRow(4) == [1, 4, 6, 4, 1]

print("Zlo")
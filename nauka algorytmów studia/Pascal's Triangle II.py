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

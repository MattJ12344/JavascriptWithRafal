from typing import List

class Solution(object):
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n: int = len(matrix)  

        topRow: int = 0
        bottomRow: int = n - 1


        while topRow < bottomRow:
            for col in range(n):
                temp:int = matrix[topRow][col]
                matrix[topRow][col] = matrix[bottomRow][col]
                matrix[bottomRow][col] = temp
                
            topRow += 1
            bottomRow -= 1

        for row in range(n):
            for col in range(row + 1, n):
                temp:int = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
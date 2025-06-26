from typing import List

class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        :type matrix: List[List[int]]
        :rtype: None
        """
        zero_positions: List[tuple[int, int]] = []
        row_count: int = len(matrix)
        col_count: int = len(matrix[0])

        for row_index in range(row_count):
            for col_index in range(col_count):
                if matrix[row_index][col_index] == 0:
                    zero_positions.append((row_index, col_index))

        for row_index, col_index in zero_positions:
            self.make_row_zero(matrix[row_index])
            self.make_column_zero(matrix, col_index)

    def make_row_zero(self, row: List[int]) -> None:
        for i in range(len(row)):
            row[i] = 0

    def make_column_zero(self, matrix: List[List[int]], col_index: int) -> None:
        for row in matrix:
            row[col_index] = 0
            
            
sol = Solution()

matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
sol.setZeroes(matrix1)
assert matrix1 == [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1]
]

matrix2 = [
    [0, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sol.setZeroes(matrix2)
assert matrix2 == [
    [0, 0, 0],
    [0, 5, 6],
    [0, 8, 9]
]

matrix3 = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [0, 10, 11, 12],
    [13, 14, 15, 0]
]
sol.setZeroes(matrix3)
assert matrix3 == [
    [0, 0, 3, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("ROBIE")
from typing import List

class Solution(object):
    def generateMatrix(self, size: int) -> List[List[int]]:
        """
        :type size: int
        :rtype: List[List[int]]
        """
        x: int = 0
        y: int = 0
        dx: int = 1
        dy: int = 0
        matrix: List[List[int]] = [[0 for _ in range(size)] for _ in range(size)]

        for value in range(1, size * size + 1):
            matrix[y][x] = value

            if not (0 <= x + dx < size and 0 <= y + dy < size) or matrix[y + dy][x + dx] != 0:
                dx, dy = -dy, dx  

            x += dx
            y += dy

        return matrix
    
    
sol = Solution()

assert sol.generateMatrix(1) == [[1]]

assert sol.generateMatrix(2) == [
    [1, 2],
    [4, 3]
]

assert sol.generateMatrix(3) == [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]

assert sol.generateMatrix(4) == [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

print("RAZ")
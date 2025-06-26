from typing import List

class Solution(object):
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        x: int = 0
        y: int = 0
        dx: int = 1
        dy: int = 0
        result: List[int] = []

        for _ in range(rows * cols):
            result.append(matrix[y][x])
            matrix[y][x] = "."  

            if not (0 <= x + dx < cols and 0 <= y + dy < rows) or matrix[y + dy][x + dx] == ".":
                dx, dy = -dy, dx  

            x += dx
            y += dy

        return result
    
sol = Solution()

assert sol.spiralOrder([[1]]) == [1]

assert sol.spiralOrder([[1, 2], [4, 3]]) == [1, 2, 3, 4]

assert sol.spiralOrder([[1, 2, 3], [8, 9, 4], [7, 6, 5]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

assert sol.spiralOrder([[1, 2, 3, 4]]) == [1, 2, 3, 4]

assert sol.spiralOrder([[1], [2], [3], [4]]) == [1, 2, 3, 4]

print("Kocham ")
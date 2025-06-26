from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
     
        rows, cols = len(grid), len(grid[0])
        perimeter: int = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += 4
                    if row > 0 and grid[row - 1][col] == 1:
                        perimeter -= 2
                    if col > 0 and grid[row][col - 1] == 1:
                        perimeter -= 2

        return perimeter


sol = Solution()

assert sol.islandPerimeter([
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]) == 16

assert sol.islandPerimeter([[1]]) == 4

assert sol.islandPerimeter([[1, 1]]) == 6

assert sol.islandPerimeter([[1], [1]]) == 6

assert sol.islandPerimeter([[0,0],[0,0]]) == 0

assert sol.islandPerimeter([[0]]) == 0

print("OK")
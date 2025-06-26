from typing import List

class Solution(object):
    def count_paths(self, row: int, col: int, max_row: int, max_col: int, memo: List[List[int]]) -> int:
        if row == max_row and col == max_col:
            return 1
        if row > max_row or col > max_col:
            return 0
        if memo[row][col] != -1:
            return memo[row][col]
        
        move_right: int = self.count_paths(row, col + 1, max_row, max_col, memo)
        move_down: int = self.count_paths(row + 1, col, max_row, max_col, memo)
        
        memo[row][col] = move_right + move_down
        return memo[row][col]

    def uniquePaths(self, rows: int, cols: int) -> int:
        """
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if rows == 0 or cols == 0:
            return 0 
        memo: List[List[int]] = [[-1] * cols for _ in range(rows)]
        return self.count_paths(0, 0, rows - 1, cols - 1, memo) % (2 * 10**9)

sol = Solution()

assert sol.uniquePaths(1, 1) == 1
assert sol.uniquePaths(2, 2) == 2
assert sol.uniquePaths(3, 2) == 3
assert sol.uniquePaths(3, 3) == 6
assert sol.uniquePaths(4, 4) == 20
assert sol.uniquePaths(5, 5) == 70
assert sol.uniquePaths(1, 10) == 1
assert sol.uniquePaths(0, 5) == 0
assert sol.uniquePaths(10, 1) == 1
assert sol.uniquePaths(10, 10) == 48620


print("cos")
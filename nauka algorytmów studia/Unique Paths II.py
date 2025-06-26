from typing import List

class Solution(object):
    def rec(
        self,
        row: int,
        col: int,
        obstacle_grid: List[List[int]],
        max_row: int,
        max_col: int,
        dp: List[List[int]]
    ) -> int:
        if row == max_row and col == max_col:
            return 1
        if row > max_row or col > max_col or obstacle_grid[row][col] == 1:
            return 0
        if dp[row][col] != -1:
            return dp[row][col]
        dp[row][col] = self.rec(row, col + 1, obstacle_grid, max_row, max_col, dp) + \
                       self.rec(row + 1, col, obstacle_grid, max_row, max_col, dp)
        return dp[row][col]

    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        """
        :type obstacle_grid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacle_grid), len(obstacle_grid[0])
        if obstacle_grid[m - 1][n - 1] == 1:
            return 0
        dp = [[-1] * n for _ in range(m)]
        return self.rec(0, 0, obstacle_grid, m - 1, n - 1, dp)
    
sol = Solution()


# Test 1
assert sol.uniquePathsWithObstacles([[0, 0], [0, 0]]) == 2

# Test 2
assert sol.uniquePathsWithObstacles([[0, 0], [0, 1]]) == 0

# Test 3
assert sol.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 6

# Test 4
assert sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2

# Test 5
assert sol.uniquePathsWithObstacles([[1, 0], [0, 0]]) == 0

# Test 6
assert sol.uniquePathsWithObstacles([[0]]) == 1

# Test 7
assert sol.uniquePathsWithObstacles([[1]]) == 0

print("lody")
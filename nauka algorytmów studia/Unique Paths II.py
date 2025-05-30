class Solution(object):
    def rec(self, r, c, obstacle, m, n, dp):
        if r == m and c == n:
            return 1
        if r > m or c > n or obstacle[r][c] == 1:
            return 0
        if dp[r][c] != -1:
            return dp[r][c]
        dp[r][c] = self.rec(r, c + 1, obstacle, m, n, dp) + self.rec(r + 1, c, obstacle, m, n, dp)
        return dp[r][c]

    def uniquePathsWithObstacles(self, obstacle):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacle), len(obstacle[0])
        if obstacle[m - 1][n - 1] == 1:
            return 0
        dp = [[-1] * n for _ in range(m)]
        return self.rec(0, 0, obstacle, m - 1, n - 1, dp)
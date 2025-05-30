class Solution(object):
    def rec(self, r, c, m, n, dp):
        if r == m and c == n:
            return 1
        if r > m or c > n:
            return 0
        if dp[r][c] != -1:
            return dp[r][c]
        
        right = self.rec(r, c + 1, m, n, dp)
        down = self.rec(r + 1, c, m, n, dp)
        
        dp[r][c] = right + down
        return dp[r][c]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1] * n for _ in range(m)]
        return self.rec(0, 0, m - 1, n - 1, dp) % (2 * 1000000000)
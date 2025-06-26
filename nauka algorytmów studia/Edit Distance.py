class Solution(object):
    def minDistance(self, word1:str, word2:str) -> int:
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m:int = len(word1)
        n:int = len(word2)

        dp:list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            
            for j in range(1, n + 1):
                
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]
    
sol = Solution()

assert sol.minDistance("horse", "ros") == 3      
assert sol.minDistance("intention", "execution") == 5
assert sol.minDistance("abc", "abc") == 0
assert sol.minDistance("abc", "def") == 3
assert sol.minDistance("", "abc") == 3
assert sol.minDistance("abc", "") == 3
assert sol.minDistance("", "") == 0

print("OMG!")
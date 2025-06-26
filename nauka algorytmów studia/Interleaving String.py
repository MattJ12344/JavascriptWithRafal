class Solution(object):
    def isInterleave(self, first: str, second: str, third: str) -> bool:
        firstLength: int = len(first)
        secondLength: int = len(second)

        if firstLength + secondLength != len(third):
            return False

        dp: list[bool] = [False] * (secondLength + 1)
        dp[0] = True

        for j in range(1, secondLength + 1):
            dp[j] = dp[j - 1] and second[j - 1] == third[j - 1]

        for i in range(1, firstLength + 1):
            dp[0] = dp[0] and first[i - 1] == third[i - 1]

            for j in range(1, secondLength + 1):
                dp[j] = (dp[j] and first[i - 1] == third[i + j - 1]) or \
                        (dp[j - 1] and second[j - 1] == third[i + j - 1])

        return dp[secondLength]
    
sol = Solution()

assert sol.isInterleave("aab", "axy", "aaxaby") == True

assert sol.isInterleave("aab", "axy", "abaaxy") == False

assert sol.isInterleave("", "", "") == True

assert sol.isInterleave("", "abc", "abc") == True

assert sol.isInterleave("abc", "", "abc") == True

assert sol.isInterleave("abc", "def", "abcd") == False

assert sol.isInterleave("aa", "ab", "aaba") == True

assert sol.isInterleave("aa", "ab", "abaa") == True

assert sol.isInterleave("abc", "def", "adbcef") == True

assert sol.isInterleave("abc", "def", "abdecf") == True

print("OKI")
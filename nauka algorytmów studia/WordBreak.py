def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    word_set: set[str] = set(wordDict)  
    dp: list[bool] = [False] * (len(s) + 1)
    dp[0] = True  

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]
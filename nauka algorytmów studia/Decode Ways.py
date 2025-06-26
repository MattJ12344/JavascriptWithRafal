class Solution(object):
    def numDecodings(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        
        n:int = len(s)
        dp:list[int] = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            one:int = int(s[i - 1])
            two:int = int(s[i - 2:i])

            if 1 <= one <= 9:
                dp[i] += dp[i - 1]
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
    
sol = Solution()

assert sol.numDecodings("12") == 2       
assert sol.numDecodings("226") == 3      
assert sol.numDecodings("06") == 0       
assert sol.numDecodings("0") == 0       
assert sol.numDecodings("10") == 1      
assert sol.numDecodings("2101") == 1     
assert sol.numDecodings("27") == 1       
assert sol.numDecodings("11106") == 2   
assert sol.numDecodings("100") == 0      
assert sol.numDecodings("1") == 1 

print("nuda")
class Solution(object):
    def generateParenthesis(self, n: int) -> list[str]:
        """
        :type n: int
        :rtype: List[str]
        """
        combinations: list[str] = []

        def dfs(openCount:int, closeCount: int, formatString: str) -> None:
            
            if openCount == closeCount and openCount + closeCount == n * 2:
                combinations.append(formatString)
                return
            
            if openCount < n:
                dfs(openCount + 1, closeCount, formatString + "(")
            
            if closeCount < openCount:
                dfs(openCount, closeCount + 1, formatString + ")")

        dfs(0, 0, "")

        return combinations
    
sol = Solution()

assert set(sol.generateParenthesis(1)) == {"()"}
assert set(sol.generateParenthesis(2)) == {"(())", "()()"}
assert set(sol.generateParenthesis(3)) == {"((()))", "(()())", "(())()", "()(())", "()()()"}
assert len(sol.generateParenthesis(4)) == 14
assert len(sol.generateParenthesis(5)) == 42

print("Spoko")
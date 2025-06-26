class Solution(object):
    def isSubsequence(self, s:str, t:str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sp:int = 0
        tp:int = 0

        while sp < len(s) and tp < len(t):
            
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)
    
sol = Solution()

assert sol.isSubsequence("abc", "ahbgdc") == True     
assert sol.isSubsequence("axc", "ahbgdc") == False    
assert sol.isSubsequence("", "anything") == True      
assert sol.isSubsequence("abc", "") == False          
assert sol.isSubsequence("ace", "abcde") == True      
assert sol.isSubsequence("aec", "abcde") == False     
assert sol.isSubsequence("a", "a") == True
assert sol.isSubsequence("a", "b") == False

print("O matko")
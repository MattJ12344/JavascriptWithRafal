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
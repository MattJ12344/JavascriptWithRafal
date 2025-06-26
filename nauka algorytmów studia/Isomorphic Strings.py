class Solution(object):
    def isIsomorphic(self, s:str, t:str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1: list[int] = []
        map2: list[int] = []
        
        for letter in s:
            map1.append(s.index(letter))
            
        for letter in t:
            map2.append(t.index(letter))
            
        if map1 == map2:
            return True
        
        return False
    
sol = Solution()

assert sol.isIsomorphic("egg", "add") == True
assert sol.isIsomorphic("foo", "bar") == False
assert sol.isIsomorphic("paper", "title") == True
assert sol.isIsomorphic("ab", "aa") == False
assert sol.isIsomorphic("badc", "baba") == False

print("BTS")
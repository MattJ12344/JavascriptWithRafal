class Solution(object):
    def longestPalindrome(self, s: str) -> int:
        
        """
        :type s: str
        :rtype: int
        """
        
        count: int = 0
        letterToCounter: dict[str, int] = {} //mapa
        
        for letter in s:
            if letter in letterToCounter:
                letterToCounter[letter] += 1
            else:
                letterToCounter[letter] = 1
            if letterToCounter[letter] % 2 == 1:
                count += 1
            else:
                count -= 1
                
        if count > 1:
            return len(s) - count + 1
        
        return len(s)
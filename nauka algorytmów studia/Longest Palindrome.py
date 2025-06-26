class Solution(object):
    def longestPalindrome(self, s: str) -> int:
        
        """
        :type s: str
        :rtype: int
        """
        
        count: int = 0
        letterToCounter: dict[str, int] = {} #mapa
        
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
    
sol = Solution()

assert sol.longestPalindrome("abccccdd") == 7   # "dccaccd"
assert sol.longestPalindrome("a") == 1
assert sol.longestPalindrome("aa") == 2
assert sol.longestPalindrome("aaa") == 3
assert sol.longestPalindrome("abc") == 1
assert sol.longestPalindrome("") == 0

print("Cosiek")
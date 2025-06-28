class Solution(object):
    def validPalindrome(self, text: str) -> bool:
        """
        :type text: str
        :rtype: bool
        """
        def is_palindrome(s: str, left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(text) - 1
        while left < right:
            if text[left] != text[right]:
                return is_palindrome(text, left + 1, right) or is_palindrome(text, left, right - 1)
            left += 1
            right -= 1
        return True
    
    
sol = Solution()

assert sol.validPalindrome("racecar") == True
assert sol.validPalindrome("raceecer") == False
assert sol.validPalindrome("abca") == True
assert sol.validPalindrome("abcdef") == False
assert sol.validPalindrome("a") == True
assert sol.validPalindrome("deeee") == True
assert sol.validPalindrome("abcdedcbg") == False  
assert sol.validPalindrome("abcdecba") == True
print("Nuda")
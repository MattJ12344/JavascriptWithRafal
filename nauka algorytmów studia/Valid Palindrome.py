class Solution(object):
    def isPalindrome(self, input_str: str) -> bool:
        """
        :type input_str: str
        :rtype: bool
        """
        cleaned: str = ''.join(char.lower() for char in input_str if char.isalnum())
        left: int = 0
        right: int = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True
    
sol = Solution()

# Test 1
assert sol.isPalindrome("A man, a plan, a canal: Panama") == True

# Test 2
assert sol.isPalindrome("race a car") == False

# Test 3
assert sol.isPalindrome("") == True

# Test 4
assert sol.isPalindrome(".,!@#") == True

# Test 5
assert sol.isPalindrome("z") == True

# Test 6
assert sol.isPalindrome("12321") == True

# Test 7
assert sol.isPalindrome("123456") == False

# Test 8
assert sol.isPalindrome("NoOn") == True

print("zrobione")
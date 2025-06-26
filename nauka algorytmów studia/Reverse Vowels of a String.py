class Solution(object):
    def reverseVowels(self, letter: str) -> str:
        """
        :type letter: str
        :rtype: str
        """
        vowels: set[str] = set("aeiouAEIOU")
        characters: list[str] = list(letter)

        left: int = 0
        right: int = len(characters) - 1

        while left < right:
            while left < right and characters[left] not in vowels:
                left += 1
            while left < right and characters[right] not in vowels:
                right -= 1

            characters[left], characters[right] = characters[right], characters[left]
            left += 1
            right -= 1

        return "".join(characters)
    
sol = Solution()

# Test 1
assert sol.reverseVowels("hello") == "holle"

# Test 2
assert sol.reverseVowels("leetcode") == "leotcede"

# Test 3
assert sol.reverseVowels("aA") == "Aa"

# Test 4
assert sol.reverseVowels("bcdfg") == "bcdfg"

# Test 5
assert sol.reverseVowels("") == ""

# Test 6
assert sol.reverseVowels("aeiou") == "uoiea"

print("Co teraz")
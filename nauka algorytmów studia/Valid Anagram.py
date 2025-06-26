from typing import List

class Solution(object):
    def isAnagram(self, str1: str, str2: str) -> bool:
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if len(str1) != len(str2):
            return False

        freq_str1: List[int] = [0] * 26
        freq_str2: List[int] = [0] * 26

        for i in range(len(str1)):
            freq_str1[ord(str1[i]) - ord('a')] += 1
            freq_str2[ord(str2[i]) - ord('a')] += 1

        return freq_str1 == freq_str2
    
sol = Solution()

# Test 1
assert sol.isAnagram("anagram", "nagaram") == True

# Test 2
assert sol.isAnagram("rat", "carrot") == False

# Test 3
assert sol.isAnagram("hello", "bello") == False

# Test 4
assert sol.isAnagram("", "") == True

# Test 5
assert sol.isAnagram("a", "a") == True

# Test 6
assert sol.isAnagram("a", "b") == False

# Test 7
assert sol.isAnagram("aabbcc", "abcabc") == True

print("kot")
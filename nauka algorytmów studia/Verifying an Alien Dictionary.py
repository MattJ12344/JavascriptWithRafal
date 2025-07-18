from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index: dict[str, int] = {c: i for i, c in enumerate(order)}
        
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for s1, s2 in zip(a, b):
                if index[s1] < index[s2]:
                    break
                elif index[s1] > index[s2]:
                    return False
        return True
    


sol = Solution()
assert sol.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True

assert sol.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") == False

assert sol.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") == False

assert sol.isAlienSorted(["app", "apple"], "abcdefghijklmnopqrstuvwxyz") == True

assert sol.isAlienSorted(["app", "app"], "abcdefghijklmnopqrstuvwxyz") == True

assert sol.isAlienSorted(
    ["a", "ab", "abc", "abcd", "abcde"],
    "abcdefghijklmnopqrstuvwxyz"
) == True

assert sol.isAlienSorted(
    ["a", "ab", "z", "abc"],
    "abcdefghijklmnopqrstuvwxyz"
) == False

assert sol.isAlienSorted(
    ["zyx", "zy", "z"],
    "zyxwvutsrqponmlkjihgfedcba"
) == False


assert sol.isAlienSorted(["same", "same", "same"], "abcdefghijklmnopqrstuvwxyz") == True

assert sol.isAlienSorted(["bcd", "abc"], "abcdefghijklmnopqrstuvwxyz") == False

assert sol.isAlienSorted([], "abcdefghijklmnopqrstuvwxyz") == True

print("nuda")
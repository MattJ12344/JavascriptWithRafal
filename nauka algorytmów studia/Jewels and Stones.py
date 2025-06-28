class Solution(object):
    def numJewelsInStones(self, jewel_types: str, stone_collection: str) -> int:
        """
        :type jewel_types: str
        :type stone_collection: str
        :rtype: int
        """
        jewel_set: set[str] = set(jewel_types)
        return sum(stone in jewel_set for stone in stone_collection)


sol = Solution()

assert sol.numJewelsInStones("aA", "aAAbbbb") == 3

assert sol.numJewelsInStones("z", "ZZZZ") == 0

assert sol.numJewelsInStones("abc", "abcabcabc") == 9

assert sol.numJewelsInStones("xYz", "xyzXYZ") == 3

assert sol.numJewelsInStones("", "abc") == 0

assert sol.numJewelsInStones("abc", "") == 0

assert sol.numJewelsInStones("aaA", "aAAbbbb") == 3

print("Nuda")
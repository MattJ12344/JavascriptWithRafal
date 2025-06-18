class Solution(object):
    def groupAnagrams(self, letters: list[str]) -> list[list[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)

        for s in letters:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        
        return list(result.values())
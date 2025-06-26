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


sol = Solution()

assert sorted([sorted(group) for group in sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])]) == \
       sorted([sorted(group) for group in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]])

assert sorted([sorted(group) for group in sol.groupAnagrams([""])]) == [[""]]

assert sorted([sorted(group) for group in sol.groupAnagrams(["a"])]) == [["a"]]

assert sorted([sorted(group) for group in sol.groupAnagrams(["abc", "bca", "cab", "xyz", "zyx"])]) == \
       sorted([["abc", "bca", "cab"], ["xyz", "zyx"]])

print("✅ Wszystkie testy przeszły poprawnie.")


##to z chatu gpt wziąłem, bo nie wiedziałem jak zrobić ten tutaj test
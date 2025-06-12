class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = {}

        for c in t:
            count[c] = count.get(c, 0) + 1

        for c in s:
            count[c] -= 1
            if count[c] == 0:
                del count[c]

        return list(count.keys())[0]
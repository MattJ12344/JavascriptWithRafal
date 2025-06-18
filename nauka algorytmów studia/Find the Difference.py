class Solution(object):
    def findTheDifference(self, s:str, t:str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letterToCounter: dict[str, int]= {}

        for letter in t:
            letterToCounter[letter] = letterToCounter.get(letter, 0) + 1

        for letter in s:
            
            letterToCounter[letter] -= 1
            
            if letterToCounter[letter] == 0:
                del letterToCounter[letter]

        return list(letterToCounter.keys())[0]
class Solution(object):
    def letterCombinations(self, keyboardKeys:str) -> list[str]:
        """
        :type digits: str
        :rtype: List[str]
        """
        if not keyboardKeys:
            return []
        
        phone: dict[str, str] = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result: list[str] = []
        
        def backtrack(combination, nextKeyboardKeys):
            if not nextKeyboardKeys:
                result.append(combination)
                return
            
            for letter in phone[nextKeyboardKeys[0]]:
                backtrack(combination + letter, nextKeyboardKeys[1:])
        
        backtrack("", keyboardKeys)
        return result
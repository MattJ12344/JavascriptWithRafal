class Solution(object):
    def titleToNumber(self, columnTitle: str) -> int:
        """
        :type columnTitle: str
        :rtype: int
        """
        result: int = 0
        
        for letter in columnTitle:
            result = result * 26 +(ord(letter) - 64)
            
        return result
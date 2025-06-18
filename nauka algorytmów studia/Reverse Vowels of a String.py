class Solution(object):
    def reverseVowels(self, letter:str) -> str:
        """
        :type s: str
        :rtype: str
        """
        vowels: set[str] = set("aeiouAEIOU")
        
        letter:str = list(letter)
        
        i:int = 0, 
        j:int = len(letter) - 1
        
        while i < j:
            
            while i < j and letter[i] not in vowels:
                i += 1
                
            while i < j and letter[j] not in vowels:
                j -= 1
                
            letter[i], letter[j] = letter[j], letter[i]
            
            i += 1
            j -= 1
            
        return "".join(letter)
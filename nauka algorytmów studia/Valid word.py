class Solution(object):
 
    def isValid(self, word:str) -> bool:
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        vowels:int = 0
        consonants:int = 0
        vowelSet:str = "aeiouAEIOU"

        for i in word:
           #if i.isalpha():
            if isAlpha(i):
                if i in vowelSet:
                    vowels += 1
                else:
                    consonants += 1
            elif not isDigit(i):
                return False 

        return vowels >= 1 and consonants >= 1
    
    
def isAlpha(letter: str) -> bool:
        return ('a' <= letter <= 'z') or ('A' <= letter <= 'Z')
    
    
def isDigit(letter: str) -> bool:
        return '0' <= letter <= '9'
        
    
sol = Solution()

assert sol.isValid("234Adas") == True

assert sol.isValid("bcd3") == False

assert sol.isValid("cos") == True

assert sol.isValid("2") == False

assert sol.isValid("Nudaa2344") == True

assert sol.isValid("####") == False

assert sol.isValid("09012@#$") == False

assert sol.isValid("234Adas#") == False

assert sol.isValid(" ") == False

assert sol.isValid("") == False

assert sol.isValid("aBCdefGhijKLMnopQRStuvWXYZabcdefgHIJKLMNOpqrstuvwxy1234567890abcdefghijklmnopqrst") == True


assert sol.isValid("aBCdefGhijKLMnopQRStuvWXYZabcdefgHIJKLMNO^pqrstuvwxy1234567890abcdefghijklmnopqrstsajdhasjkdhkdhaskjdhasjkhdkasdadiuhuwqiheiqwh009909") == False

print("Nuda")

    
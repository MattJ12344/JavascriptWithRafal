class Solution:
    def countSegments(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        countWords: int = 0

        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                countWords += 1
                
        return countWords
    
sol = Solution()

assert sol.countSegments("") == 0                     
assert sol.countSegments("    ") == 0                   
assert sol.countSegments("Hello") == 1                    
assert sol.countSegments("Hello world") == 2                
assert sol.countSegments("   Hello   world  ") == 2         
assert sol.countSegments("a b c d e") == 5                  
assert sol.countSegments("This is a test.") == 4            
assert sol.countSegments("One  two   three") == 3           
assert sol.countSegments("Hi! How are you?") == 4           

print("Nuda")
class Solution(object):
    def intToRoman(self, number: int) -> str:
        """
        :type num: int
        :rtype: str
        """
        Roman:str = ""
        storeIntRoman: list[list[object]]  = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"],   [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        
        for i in range(len(storeIntRoman)):
            while number >= storeIntRoman[i][0]:
                Roman += storeIntRoman[i][1]
                number -= storeIntRoman[i][0]
                
                
        return Roman
    
sol = Solution()

assert sol.intToRoman(1) == "I"
assert sol.intToRoman(3) == "III"
assert sol.intToRoman(4) == "IV"
assert sol.intToRoman(9) == "IX"
assert sol.intToRoman(58) == "LVIII"       
assert sol.intToRoman(1994) == "MCMXCIV"   
assert sol.intToRoman(3999) == "MMMCMXCIX" 
assert sol.intToRoman(44) == "XLIV"
assert sol.intToRoman(621) == "DCXXI"
assert sol.intToRoman(2024) == "MMXXIV"

print("Kokoszka")
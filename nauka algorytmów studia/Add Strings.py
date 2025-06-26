class Solution(object):
    def addStrings(self, number1: str, number2:str) -> str:
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
         
        def strToInt(number:str) -> int :
            numberDictonary: dict[str, int] = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                  '6' : 6, '7' : 7, '8' : 8, '9' : 9}
            output: int = 0
            
            for digit in number:
                output = output * 10 + numberDictonary[digit]
            return output
        
        
        return str(strToInt(number1) + strToInt(number2)) 
    

sol=Solution()

assert sol.addStrings('23', '34') == '57'
assert sol.addStrings('11', '123') == '134'
assert sol.addStrings('456', '77') == '533'
assert sol.addStrings('0', '0') == '0'
assert sol.addStrings('10000000000', '10000000000') == '20000000000'

print("ktos")
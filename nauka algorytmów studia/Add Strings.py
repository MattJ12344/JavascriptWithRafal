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
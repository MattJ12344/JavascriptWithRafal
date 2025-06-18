class Solution(object):
    def toHex(self, number:int) -> str:
        """
        :type num: int
        :rtype: str
        """
        if number == 0:
            return "0"
        
        if number < 0:
            number += 2**32
            
        h:str = "0123456789abcdef"
        
        r:list[str] = []
        
        while number:
            r.append(h[number & 15])
            number //= 16
            
        return "".join(r[::-1])
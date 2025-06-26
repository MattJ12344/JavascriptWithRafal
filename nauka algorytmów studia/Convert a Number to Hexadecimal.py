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
    

sol = Solution()

assert sol.toHex(26) == "1a"
assert sol.toHex(0) == "0"
assert sol.toHex(-1) == "ffffffff"
assert sol.toHex(16) == "10"
assert sol.toHex(255) == "ff"
assert sol.toHex(-2147483648) == "80000000"

print("jasiek")
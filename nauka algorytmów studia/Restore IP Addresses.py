class Solution(object):
    def restoreIpAddresses(self, letter: str) -> list[str]:
        """
        :type s: str
        :rtype: List[str]
        """
        validIp: list[str] = []
        
        self.dfs(letter, 0, "", validIp)
        
        return validIp
    
    def dfs(self, letter:str, index:int, currentIp:str, validIp: list[str]) -> None:
        
        if index > 4:
            return 
        
        if index == 4 and not letter:
            validIp.append(currentIp[:-1])
            return 
        
        for i in range(1, len(letter)+1):
            if letter[:i]=='0' or (letter[0]!='0' and 0 < int(letter[:i]) < 256):
                self.dfs(letter[i:], index+1, currentIp+letter[:i]+".", validIp)

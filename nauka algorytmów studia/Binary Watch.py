class Solution(object):
    def readBinaryWatch(self, turnedOn:int) -> list[str]:
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        if turnedOn < 0 or turnedOn > 10:
            return []
        
        result:list[str] = []
        for hour in range(12):
            
            for minute in range(60):
                
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    result.append("{}:{:02d}".format(hour, minute))
        
        return result
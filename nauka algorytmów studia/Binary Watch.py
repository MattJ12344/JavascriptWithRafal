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
    

sol = Solution()

assert sol.readBinaryWatch(0) == ["0:00"]

result_1 = sol.readBinaryWatch(1)
expected_1 = [
    "0:01", "0:02", "0:04", "0:08", "0:16", "0:32",
    "1:00", "2:00", "4:00", "8:00"
]
assert set(result_1) == set(expected_1)

result_2 = sol.readBinaryWatch(2)

assert "0:03" in result_2  
assert "1:01" in result_2  
assert "2:02" in result_2  
assert "3:00" in result_2  
assert "10:32" in result_2  


assert sol.readBinaryWatch(-1) == []
assert sol.readBinaryWatch(11) == []

print("Kochani")
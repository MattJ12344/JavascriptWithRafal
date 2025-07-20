from datetime import date

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return date(year, month, day).strftime("%A")
    
    
sol = Solution()

assert sol.dayOfTheWeek(31, 8, 2019) == "Saturday"  
assert sol.dayOfTheWeek(1, 1, 2000) == "Saturday"     
assert sol.dayOfTheWeek(20, 7, 1969) == "Sunday"      
assert sol.dayOfTheWeek(29, 2, 2020) == "Saturday"    
assert sol.dayOfTheWeek(15, 4, 2024) == "Monday" 

print("Nuda")
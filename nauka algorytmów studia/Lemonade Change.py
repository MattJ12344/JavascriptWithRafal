from typing import List

class Solution(object):
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        :type bills: List[int]
        :rtype: bool
        """
        fiveBill:int = 0
        tenBill:int = 0

        for b in bills:
            if b== 5:
                fiveBill += 1
                
            if b== 10:
                tenBill += 1    

            changeBill:int = b - 5

            if changeBill == 5:

                if fiveBill > 0:
                    fiveBill -= 1

                else:
                    return False

            elif changeBill == 15:

                if fiveBill > 0 and tenBill > 0:
                    fiveBill -= 1
                    tenBill -= 1

                elif fiveBill >= 3:
                    fiveBill -= 3

                else: 
                    return False

        return True
    
sol = Solution()

# Test 1
assert sol.lemonadeChange([5,5,5,10,20]) == True

# Test 2
assert sol.lemonadeChange([10]) == False

# Test 3
assert sol.lemonadeChange([5,5,10,10,20]) == False

# Test 4
assert sol.lemonadeChange([5,5,5,5]) == True

# Test 5
assert sol.lemonadeChange([5,5,10,5,5,5,10,10,10,20]) == True

# Test 6
assert sol.lemonadeChange([5,5,5,10,5,10,20]) == True

print("nuda")
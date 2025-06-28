from typing import List

class Solution(object):
    def calPoints(self, operations: List[str]) -> int:
        """
        :type operations: List[str]
        :rtype: int
        """
        score_stack: List[int] = []

        for operation in operations:
            
            if operation not in {"+", "D", "C"}:
                score_stack.append(int(operation))
                
            elif operation == "+":
                last = score_stack[-1]
                second_last = score_stack[-2]
                score_stack.append(last + second_last)
                
            elif operation == "D":
                last = score_stack[-1]
                score_stack.append(last * 2)
                
            elif operation == "C":
                score_stack.pop()
                

        return sum(score_stack)


sol = Solution()

# Test 1
assert sol.calPoints(["5", "2", "C", "D", "+"]) == 30  

# Test 2
assert sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27

# Test 3
assert sol.calPoints(["1"]) == 1

# Test 4
assert sol.calPoints(["1", "C"]) == 0

# Test 5
assert sol.calPoints(["3", "6", "+", "D", "C", "7"]) == 25  

# Test 6
assert sol.calPoints(["10", "-5", "D", "+", "C", "C", "30"]) == 35  

# Test 7 
assert sol.calPoints(["1", "D", "D", "D"]) == 15  

# Test 8 
assert sol.calPoints(["1", "2", "+", "+", "+"]) == 17  

print("Nuda")
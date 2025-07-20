from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1: int = points[0][0]
        y1: int = points[0][1]
        x2: int = points[1][0]
        y2: int = points[1][1]
        x3: int = points[2][0]
        y3: int = points[2][1]

        area: int = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        return area != 0
    
sol = Solution()

# Test 1
assert sol.isBoomerang([[1,1], [2,3], [3,2]]) == True

# Test 2
assert sol.isBoomerang([[1,1], [2,2], [3,3]]) == False

# Test 3
assert sol.isBoomerang([[1,1], [1,1], [2,2]]) == False

# Test 4
assert sol.isBoomerang([[0,0], [1,1], [1,2]]) == True

# Test 5
assert sol.isBoomerang([[0,0], [1,0], [2,0]]) == False

print("Nuda")
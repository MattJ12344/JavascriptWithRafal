from typing import List

class Solution(object):
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        :type matrix: List[List[int]]
        :rtype: None. Do not return anything, modify matrix in-place instead.
        """
        n: int = len(matrix)

        top: int = 0
        bottom: int = n - 1

        while top < bottom:
            for col in range(n):
                temp: int = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1
            
        for row in range(n):
            for col in range(row + 1, n):
                temp: int = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
                
                
sol = Solution()

# Test 1
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sol.rotate(m1)
assert m1 == [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

# Test 2 
m2 = [[1]]
sol.rotate(m2)
assert m2 == [[1]]

# Test 3
m3 = [
    [1, 2],
    [3, 4]
]
sol.rotate(m3)
assert m3 == [
    [3, 1],
    [4, 2]
]

# Test 4 
m4 = [
    [5, 1, 9,11],
    [2, 4, 8,10],
    [13, 3, 6,7],
    [15,14,12,16]
]
sol.rotate(m4)
assert m4 == [
    [15,13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7,10,11]
]


print("Mam nadzieje")

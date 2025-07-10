from typing import List

class Solution(object):
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n: int = len(image)
        for i in range(n):
            for j in range((n + 1) // 2):
                originalLeft: int = image[i][j]
                image[i][j] = image[i][n - j - 1] ^ 1
                image[i][n - j - 1] = originalLeft ^ 1
        return image
    
sol = Solution()

# Test 1
assert sol.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]

# Test 2
assert sol.flipAndInvertImage([[1,1,1],[1,1,1],[1,1,1]]) == [[0,0,0],[0,0,0],[0,0,0]]

# Test 3
assert sol.flipAndInvertImage([[0,0,0],[0,0,0],[0,0,0]]) == [[1,1,1],[1,1,1],[1,1,1]]

# Test 4
assert sol.flipAndInvertImage([[1,0],[0,1]]) == [[1,0],[0,1]]


print("Nuda")
class Solution(object):
    def minPathSum(self, matrix: list[list[int]]):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows: int = len(matrix)
        columns: int = len(matrix[0])
        
        for i in range(1, columns):
            matrix[0][i] += matrix[0][i-1]
            
        for i in range(1, rows):
            matrix[i][0] += matrix[i-1][0]
            
        for i in range(1, rows):
            
            for j in range(1, columns):
                matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
                
                
        return matrix[-1][-1]
    
sol = Solution()

assert sol.minPathSum([
    [1,3,1],
    [1,5,1],
    [4,2,1]
]) == 7  

assert sol.minPathSum([
    [1,2,3],
    [4,5,6]
]) == 12 

assert sol.minPathSum([[5]]) == 5

assert sol.minPathSum([
    [1,1,1],
    [1,1,1],
    [1,1,1]
]) == 5  

print("nuda")

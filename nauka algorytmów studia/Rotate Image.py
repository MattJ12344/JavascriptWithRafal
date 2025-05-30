class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        edge_length = len(matrix)

        top = 0
        bottom = edge_length - 1

        while top < bottom:
            for col in range(edge_length):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1

        for row in range(edge_length):
            for col in range(row+1, edge_length):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        return matrix
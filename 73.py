class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowZeros = []
        colZeros = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rowZeros.append(row)
                    colZeros.append(col)
        
        for row in rowZeros:
            matrix[row] = [0] * len(matrix[row])
        
        for i in range(len(matrix)):
            for col in colZeros:
                matrix[i][col] = 0
        
        return matrix

obj = Solution()
print(obj.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
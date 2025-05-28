class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        leftRow = 0
        midRow = 0
        rightRow = len(matrix) - 1
        
        targetRow = 0
        
        while leftRow <= rightRow:
            midRow = (leftRow + rightRow) // 2
            
            if target in matrix[midRow]:
                targetRow = midRow
                break
            elif matrix[midRow][0] < target:
                leftRow = midRow + 1
            elif matrix[midRow][0] > target:
                rightRow = midRow - 1
        
        low = 0
        mid = 0
        high = len(matrix[0]) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if matrix[targetRow][mid] < target:
                low = mid + 1
            elif matrix[targetRow][mid] > target:
                high = mid - 1
            else:
                return True
        
        return False

obj = Solution()
print(obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))
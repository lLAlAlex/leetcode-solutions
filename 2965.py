class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        max_val = len(grid[1])**2
        nums = set()
        dup = []
        missing = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in nums:
                    dup.append(grid[i][j])
                else:
                    nums.add(grid[i][j])
        
        num_arr = list(nums)
        
        for i in range(1, max_val+1):
            if i not in num_arr:
                missing = i
                break
                    
        return dup + [missing]
        
obj = Solution()
print(obj.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))
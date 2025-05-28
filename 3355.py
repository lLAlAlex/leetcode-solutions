import numpy as np

class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        temp = np.array([0] * len(nums))
        
        for query in queries:
            temp[query[0]:query[1] + 1] += 1
        
        for i in range(len(nums)):
            if nums[i] > temp[i]:
                return False
    
        return True

obj = Solution()
print(obj.isZeroArray([1,2,1,0,0,0], [[0,3],[2,4]]))
class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEnding = minEnding = maxRes = minRes = nums[0]
        
        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            maxRes = max(maxEnding, maxRes)
            
            minEnding = min(minEnding + nums[i], nums[i])
            minRes = min(minEnding, minRes)
        
        return max(abs(minRes), abs(maxRes))
        
obj = Solution()
print(obj.maxAbsoluteSum([-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9]))
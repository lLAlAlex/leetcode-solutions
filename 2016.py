class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        
        res = -1
        
        for i in range(len(nums)):
            if nums[i] > temp:
                res = max(res, nums[i] - temp)
            else:
                temp = nums[i]
        
        return res

obj = Solution()
print(obj.maximumDifference([7,1,5,4]))
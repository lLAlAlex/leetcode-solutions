class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = 0
        
        for i in range(len(nums)):
            if nums[i] < 0:
                neg += 1
            
            if nums[i] > 0 and neg > len(nums) - i:
                return neg
            
            if nums[i] > 0 and neg < len(nums) - i:
                return len(nums) - i
        
        return neg

obj = Solution()
print(obj.maximumCount([-1764,-1562,-1226,-1216,-402,-386,-133,979,1227,1992]))
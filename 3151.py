class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and i+1 < len(nums):
                if nums[i+1] % 2 == 0:
                    return False
            
            if nums[i] % 2 != 0 and i+1 < len(nums):
                if nums[i+1] % 2 != 0:
                    return False
                
        return True

obj = Solution()
print(obj.isArraySpecial([4,3,1,6]))
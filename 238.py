class Solution(object):
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        
        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        
        return res

obj = Solution()
obj.productExceptSelf([-1,0,1,2,3])